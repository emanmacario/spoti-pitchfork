import json
import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth
from spotify_client_credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, USERNAME

# Spotify Search API Link: https://developer.spotify.com/documentation/web-api/reference/search/search/

# scope = 'playlist-modify-public'

def search_for_track(artist, track):
    """
    Uses the Spotify search API to search for a track for a given artist
    :param artist: artist name
    :param track: track name
    :param debug: True or False indicating whether to write search results to a JSON file
    :return: Spotify track ID
    """
    # Initialise the Spotify API by setting scope and credentials
    scope = 'user-library-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                                   client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   username=USERNAME))
    # Perform the search
    result = sp.search(q=f"artist:{artist} track:{track}", type="track", limit=1)
    # pprint(result)

    # Debugging
    debug = False
    if debug:
        with open('result.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4)

    print('-'*50)
    print(f"Searched for track '{track}' by '{artist}'")
    items = result['tracks']['items']

    if len(items) > 0:
        track_uri = result['tracks']['items'][0]['uri']
        print(f"Found track: {track_uri}")
    else:
        track_uri = None
        print("Track not found on Spotify")

    return track_uri



def search_for_album(artist, album):
    """
    Uses the Spotify search API to search for an album for a given artist
    :param artist: artist name
    :param album: album name
    :return: Spotify album ID
    """
    # Initialise the Spotify API by setting scope and credentials
    scope = 'user-library-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                                   client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   username=USERNAME))

    # Perform the search
    result = sp.search(q=f"artist:{artist} album:{album}", type="album", limit=1)

    # Debugging
    debug = True
    if debug:
        with open('result-album.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4)

    print('-' * 50)
    print(f"Searched for album '{album}' by '{artist}'")
    items = result['albums']['items']

    if len(items) > 0:
        album_uri = result['albums']['items'][0]['uri']
        print(f"Found album: {album_uri}")
    else:
        album_uri = None
        print("Album not found on Spotify")

    return album_uri


def search_for_tracks(tracks):
    """
    Uses the Spotify search API to search for a list of tracks
    :param tracks: list of track dictionaries
    :return: list of Spotify track IDs
    """
    track_ids = []
    for entry in tracks:
        artist = entry['artist']
        track = entry['track']
        track_uri = search_for_track(artist, track)

        if track_uri is not None:
            track_ids.append(track_uri)

    return track_ids



def search_for_tracks_kwargs(albums):
    """
    Uses the Spotify search API to search for albums,
    and return the track IDs of those albums
    :param albums: list of album dictionaries
    :return: list of Spotify track IDs
    """
    track_ids = []
    for entry in albums:
        artist = entry['artist']
        album = entry['album']
        print('-'*50)
        print(f"Searching for tracks for album '{album}' by '{artist}'")
        album_id = search_for_album(artist, album)

        scope = 'user-library-read'
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                                       client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri=REDIRECT_URI,
                                                       username=USERNAME))
        if album_id is not None:
            print("Album found!")
            res = sp.album_tracks(album_id)
            for track in res['items']:
                track_id = track['id']
                track_ids.append(track_id)

            debug = False
            if debug:
                with open('result-album-tracks.json', 'w', encoding='utf-8') as f:
                    json.dump(res, f, indent=4)
        else:
            print("Album not found!")

    return track_ids




def search_for_albums(albums):
    """
    Uses the Spotify search API to search for a list of albums
    :param tracks: A list of track dictionaries
    :return: list of Spotify album IDs
    :param albums: list of album dictionaries
    :return: list of Spotify album IDs
    """
    album_ids = []
    for entry in albums:
        artist = entry['artist']
        album = entry['album']
        album_uri = search_for_album(artist, album)
        if album_uri is not None:
            album_ids.append(album_uri)

    return album_ids



from pitchfork_rss import get_best_new_tracks, get_best_new_albums

if __name__ == "__main__":
    """
    best_new_tracks = get_best_new_tracks()
    for entry in best_new_tracks:
        artist = entry['artist']
        track = entry['track']
        search_for_track(artist, track)
    """
    # best_new_albums = get_best_new_albums()
    # for entry in best_new_albums:
    #     artist = entry['artist']
    #     album = entry['album']
    #     search_for_album(artist, album)

    best_new_albums = get_best_new_albums()
    search_for_tracks_kwargs(best_new_albums)







