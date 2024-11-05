from dataclasses import dataclass


@dataclass
class Song: 
    title: str
    artist: str
    genre: str
    album: str
    album_image: str
    youtube_id: str
    tab: str
    lyrics: str