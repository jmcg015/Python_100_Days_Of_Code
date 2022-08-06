import requests
import pprint
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input("What year would you like to go to? Type the date like this YYYY-MM-DD:  ")
year = date.split("-")[0]

url = f"https://www.billboard.com/charts/hot-100/{date}"

clientID = "HIDDEN"
clientSecret = "HIDDEN"
REDIRECT_URI = "http://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=clientID,
        client_secret=clientSecret,
        redirect_uri=REDIRECT_URI,
        scope="playlist-modify-private",
        cache_path="token2.txt",
        show_dialog=True,
    )
)

user_id = sp.current_user()['id']

response = requests.get(url)
billboard_web_page = response.text
soup = BeautifulSoup(billboard_web_page, "html.parser")

all_songs = soup.find_all("h3", id="title-of-a-story",  class_="u-letter-spacing-0021")
song_titles = [song.getText().strip() for song in all_songs]

values_to_be_removed = ['Songwriter(s):', 'Producer(s):', 'Imprint/Promotion Label:',]

song_names = []

for title in song_titles:
    if title != 'Songwriter(s):' and title != 'Producer(s):' and title != 'Imprint/Promotion Label:':
        song_names.append(title)

song_uri = []

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    #pprint.pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} not found, skipping to the next one")



new_playlist = track = sp.user_playlist_create(user=user_id,
                                    name=f"{date} Billboard 100",
                                    public=False,
                                    collaborative=False,
                                    description="Go back in time")
playlist_id = new_playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=song_uri, position=None)
