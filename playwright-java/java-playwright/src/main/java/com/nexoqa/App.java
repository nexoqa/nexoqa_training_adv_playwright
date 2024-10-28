package com.nexoqa;

import com.github.javafaker.Faker;
import com.microsoft.playwright.*;
import com.microsoft.playwright.options.AriaRole;

public class App {
    public static void main(String[] args) {
        try (Playwright playwright = Playwright.create()) {
            Faker faker = new Faker();
            Browser browser = playwright.webkit()
                    .launch(new BrowserType.LaunchOptions().setHeadless(false).setSlowMo(50));
            Page page = browser.newPage();
            page.navigate("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
            page.locator("input[name='username']").fill("Admin");
            page.locator("input[name='password']").fill("admin123");
            page.getByRole(AriaRole.BUTTON, new Page.GetByRoleOptions().setName("Login")).click();
            // Open Admin page
            page.getByRole(AriaRole.LINK, new Page.GetByRoleOptions().setName("PIM")).click();
            // Add new user
            page.getByRole(AriaRole.BUTTON, new Page.GetByRoleOptions().setName("Add")).click();
            page.locator("input[name='firstName']").fill(faker.name().firstName());
            page.locator("input[name='middleName']").fill("");
            page.locator("input[name='lastName']").fill(faker.name().lastName());
            page.locator("div.oxd-form-row.user-form-header > div > label > span").click();
            page.locator("input.oxd-input.oxd-input--active").nth(0).fill(faker.name().username());
            String password = faker.funnyName().name() + "@1A";
            page.locator("input[type='password']").nth(0).fill(password);
            page.locator("input[type='password']").nth(1).fill(password);
            page.getByRole(AriaRole.BUTTON, new Page.GetByRoleOptions().setName("Save")).click();

            assert page.getByRole(AriaRole.LINK, new Page.GetByRoleOptions().setName("Personal Details"))
                    .isVisible() == true;

        }
    }
}