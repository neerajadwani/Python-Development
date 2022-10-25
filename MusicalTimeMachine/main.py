from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']


date = input("Which year do you want to travel to? Type the date in this format YYY-MM-DD:")
response = requests.get("https://www.billboard.com/charts/hot-100/"+date)
soup = BeautifulSoup(response.text, 'html.parser')
# after inspecting the HTML page, note that each title is identified by a cascade of li ul li h3 tags
results = soup.select("li ul li h3")
# use list comprehension to strip leading and trailing spaces and create a new list of just the titles
names = [result.text.strip() for result in results]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",client_id=SPOTIPY_CLIENT_ID,
                     client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI,
                     show_dialog=True,
                     cache_path="token.txt"))
user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]
for song in names:
    result = sp.search(q=f"track{song} year{year}",type="track")
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

