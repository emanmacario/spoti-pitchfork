# Creates a playlist for a user

import argparse
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotify_client_credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, USERNAME


def get_args():
    parser = argparse.ArgumentParser(description='Creates a playlist for user')
    parser.add_argument('-p', '--playlist', required=True,
                        help='Name of Playlist')
    parser.add_argument('-d', '--description', required=False, default='',
                        help='Description of Playlist')
    return parser.parse_args()


def main():
    args = get_args()
    scope = "playlist-modify-public"
    auth_manager = SpotifyOAuth(scope=scope,
                                client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                redirect_uri=REDIRECT_URI,
                                username=USERNAME)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    user_id = sp.me()['id']
    sp.user_playlist_create(user_id, args.playlist, description=args.description)


if __name__ == '__main__':
    main()
