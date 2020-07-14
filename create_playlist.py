# Creates a playlist for a user

import argparse
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotify_client_credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, USERNAME

import json

def get_args():
    parser = argparse.ArgumentParser(description='Creates Spotify playlists for the user')
    parser.add_argument('-p', '--playlist', required=True,
                        help='Name of Playlist')
    parser.add_argument('-d', '--description', required=False, default='',
                        help='Description of Playlist')
    parser.add_argument('-t', '--tracks', action="store_true",
                        help="Create playlist for 'best new tracks'")
    parser.add_argument('-a', '--albums', action="store_true",
                        help="Create playlist for 'best new albums'")
    parser.add_argument('-r', '--reissues', action="store_true",
                        help="Create playlist for 'best new re-issues'")
    return parser.parse_args()

from pitchfork_rss import get_best_new_tracks, get_best_new_albums
from search import search_for_tracks, search_for_albums
from pprint import pprint


def create_best_new_tracks_playlist():
    args = get_args()
    scope = "playlist-modify-public"
    auth_manager = SpotifyOAuth(scope=scope,
                                client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                redirect_uri=REDIRECT_URI,
                                username=USERNAME)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    user_id = sp.me()['id']
    playlist_id = sp.user_playlist_create(user_id, args.playlist, description=args.description)['id']
    best_new_tracks = get_best_new_tracks()
    track_ids = search_for_tracks(best_new_tracks)
    sp.user_playlist_add_tracks(user_id, playlist_id, track_ids)


from pprint import pprint
from search import get_tracks_for_albums

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
    playlist_id = sp.user_playlist_create(user_id, args.playlist, description=args.description)['id']
    best_new_albums = get_best_new_albums()
    album_ids = search_for_albums(best_new_albums)

    # TODO: Use list comprehension here. Add tracks endpoint request only asccetps 100 at a time
    track_ids = get_tracks_for_albums(album_ids)
    print("TRACK IDS BOI")
    pprint(track_ids)



    track_id_chunks = [track_ids[i: i + 100] for i in range(0, len(track_ids), 100)]
    print("CHUNKS BOIY")
    pprint(track_id_chunks)
    # album_ids = search_for_albums(best_new_albums)
    for track_id_chunk in track_id_chunks:
        pprint(track_id_chunk)
        sp.user_playlist_add_tracks(user_id, playlist_id, track_id_chunk)



if __name__ == '__main__':
    main()

