import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json, pprint

import os




secret = os.getenv("SECRET")
the_client_id = os.getenv("CLIENT_ID")

breakpoint()
client_cred_manager = SpotifyClientCredentials(client_id=the_client_id, client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager=client_cred_manager)

playlists = sp.user_playlists("spotify")

breakpoint()
print(len(playlists))