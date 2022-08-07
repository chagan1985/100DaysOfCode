###################################
#
# 100 Days of code bootcamp 2022
# (Udemy course by Angela Yu)
# 
# Day 46 exercise - Christopher Hagan
#
###################################

from urllib.error import HTTPError
from httplib2 import Http
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
from bs4 import BeautifulSoup

# Values set on 'https://developer.spotify.com/dashboard/' and require setup prior to execution
SPOTIFY_CLIENT_ID = '60b60c99551945ff802e776b64ea1137'
SPOTIFY_CLIENT_SECRET = 'd56b91c7a07b40679684642f687fa25a'
REDIRECT_URI = 'http://example.com'

date = ''
song_list = []
artist_list = []

# Parse date to ensure it is valid
while date == '':
    try:
        date_input = input('Which yeah do you wish to travel to? (in the format YYYY-MM-DD): ')
        date = datetime.strptime(date_input, '%Y-%m-%d')
    except ValueError:
        print('Invalid date, please try again...')
        date = ''

# Query billboard website for top 100 songs on the date provided
response = requests.get('https://www.billboard.com/charts/hot-100/{}'.format(date.strftime('%Y-%m-%d')))
soup = BeautifulSoup(response.text, 'html.parser')

song_names_list = soup.findAll('h3', id='title-of-a-story')
for song in song_names_list:
    song_name = song.get_text().replace('\n', '').replace('\t', '').replace('\'', '')
    if song_name not in ['Songwriter(s):', 'Producer(s):', 'Imprint/Promotion Label:']:
        song_list.append(song_name)
song_list = song_list[3:103]

artist_names_list = soup.find_all(name='span', class_='c-label')
for artist in artist_names_list:
    artist_name = artist.get_text().replace('\n', '').replace('\t', '')
    if artist_name not in ['NEW', '-', 'ENTRY', 'RE-ENTRY'] and not artist_name.isnumeric():
        artist_list.append(artist_name)

# Authenticate and cache the token information, note the hardcoded values require prequisites
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user().get('id')

print(user_id)

song_uris_list = []
for i in range(100):
    try:
        song = sp.search(q='track:{} artist: {} year:{}'.format(song_list[i], artist_list[i], date.strftime('%Y'), type='track'))['tracks']['items'][0]
        song_uris_list.append(song['uri'])
    except IndexError or HTTPError:
        pass
        # print('Song doesn\'t exist in Spotify, skipping...')

# Create playlist and add those songs which URIs exist for
playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)['id']
add_items = sp.playlist_add_items(playlist_id, items=song_uris_list)
