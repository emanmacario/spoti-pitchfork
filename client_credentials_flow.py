import argparse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotify_client_credentials import CLIENT_ID, CLIENT_SECRET

# Initialise Spotify API by passing app credentials (client credentials flow)
manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=manager)

playlists = sp.user_playlists('eman1997')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None


def get_args():
    parser = argparse.ArgumentParser(description='Choose the type(s) of playlists you want created')
    parser.add_argument('-a', '--albums', required=True, help='Best new albums')
    parser.add_argument('-t', '--tracks', required=True, help='Best new tracks')
    parser.add_argument('-r', '--reissues', required=True, help='Best new reissues')
    return parser.parse_args()
