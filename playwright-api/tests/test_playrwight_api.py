from typing import Generator
import pytest

from playwright.sync_api import Playwright, APIRequestContext


@pytest.fixture(scope="session")
def create_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="http://ec2-34-245-218-17.eu-west-1.compute.amazonaws.com:8081"
    )
    yield request_context
    request_context.dispose()


def create_user(context: APIRequestContext, username: str, password: str):
    payload: dict = {"email": username, "password": password}
    headers: dict = {"content-type": "application/json; charset=utf-8"}

    return context.post(url="/register", data=payload, headers=headers)


def test_signup_valid_user(create_request_context: APIRequestContext):
    create_request_context.get("reset")

    payload: dict = {"email": "test@test2.com", "password": "87654321"}
    headers: dict = {"content-type": "application/json; charset=utf-8"}

    response = create_request_context.post(
        url="/register", data=payload, headers=headers
    )

    assert response.status == 200
    json_response = response.json()
    assert json_response["user"] is not None
    assert json_response["token"] is not None


def test_create_user_that_already_exists(create_request_context: APIRequestContext):
    create_request_context.get("reset")
    create_user(
        create_request_context, username="gpopa_1@test.com", password="12345678"
    )

    response = create_user(
        create_request_context, username="gpopa_1@test.com", password="12345678"
    )
    assert response.status == 400
    assert response.json() == {"error": "This email account is already in use."}


def test_login_valid_user(create_request_context: APIRequestContext):
    create_request_context.get("reset")

    email: str = "gpopa_1@test.com"
    password: str = "12345678"

    create_user(create_request_context, username=email, password=password)

    payload: dict = {"email": email, "password": password}
    headers: dict = {"content-type": "application/json; charset=utf-8"}

    response = create_request_context.post(url="/login", data=payload, headers=headers)

    assert response.status == 200
    json_response = response.json()
    assert json_response["user"] is not None
    assert json_response["token"] is not None


def test_login_invalid_user(create_request_context: APIRequestContext):
    create_request_context.get("reset")

    email: str = "gpopa_1@test.com"
    password: str = "12345678"

    payload: dict = {"email": email, "password": password}
    headers: dict = {"content-type": "application/json; charset=utf-8"}

    response = create_request_context.post(url="/login", data=payload, headers=headers)

    assert response.status == 403
    json_response = response.json()
    assert response.json() == {"error": "The login information was incorrect"}


def test_get_bookmarks(create_request_context: APIRequestContext):
    create_request_context.get("reset")

    email: str = "gpopa_1@test.com"
    password: str = "12345678"

    user_response = create_user(
        create_request_context, username=email, password=password
    )
    user_json_response = user_response.json()

    headers: dict = {
        "content-type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {user_json_response['token']}",
    }

    response = create_request_context.get(url="/bookmarks", headers=headers)

    assert response.status == 200
    json_response = response.json()
    assert response.json() == []


def test_post_bookmarks(create_request_context: APIRequestContext):
    # PRECONDITIONS
    create_request_context.get("reset")

    email: str = "gpopa_1@test.com"
    password: str = "12345678"

    user_response = create_user(
        create_request_context, username=email, password=password
    )
    user_json_response = user_response.json()
    user = user_json_response["user"]

    headers: dict = {
        "content-type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {user_json_response['token']}",
    }

    songs_response = create_request_context.get(url="/songs", headers=headers)
    songs_json_response = songs_response.json()

    song = songs_json_response[0]

    payload: dict = {"songId": song["id"]}

    # TEST
    response = create_request_context.post(
        url="/bookmarks", data=payload, headers=headers
    )

    assert response.status == 200
    json_response = response.json()

    assert json_response["id"] is not None
    assert json_response["SongId"] == song["id"]
    assert json_response["UserId"] == user["id"]
    assert json_response["updatedAt"] is not None
    assert json_response["createdAt"] is not None
