import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy import SpotifyOAuth

"""Scraping bill bard to fetch the top 100 songs add them to my spotify playlist """
# pass_date = input("which year do you want to travel to ? Type the date in the format YYYY-MM-DD")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
URL = "https://www.billboard.com/charts/hot-100/" + "1999-06-13"
response = requests.get(url=URL,headers=header)
movies_website = response.text
soup = BeautifulSoup(movies_website,'html.parser')
song_names_spans = soup.select("li ul li h3")
songs_name = [song.getText().strip() for song in song_names_spans ]

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=YOUR-CLIENT-ID,
        client_secret=YOUR-CLIENT-SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
