# Creates a playlist for a user
import argparse
import json
import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from spotify_client_credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, USERNAME

# Spotify Search API Link: https://developer.spotify.com/documentation/web-api/reference/search/search/


def main():
    scope = 'user-library-read'
    scope = 'user-top-read'
    auth_manager = SpotifyOAuth(scope=scope,
                                client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                redirect_uri=REDIRECT_URI,
                                username=USERNAME)

    sp = spotipy.Spotify(auth_manager=auth_manager)
    ranges = ['short_term', 'medium_term', 'long_term']

    for sp_range in ranges:
        print("range:", sp_range)
        results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
        for i, item in enumerate(results['items']):
            print(i, item['name'], '//', item['artists'][0]['name'])
        print()

    # Note: Spotipy search API doesn't require authentication
    artist = 'Kelly Lee Owens'
    track = 'Melt!'
    result = sp.search(q=f"artist:{artist} track:{track}", type="track")
    pprint.pprint(result)

    debug = True
    if debug:
        with open('result.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4)






if __name__ == "__main__":
    main()

