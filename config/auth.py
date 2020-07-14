import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config.spotify_client_credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, USERNAME, SCOPE

# Initialise Spotify API by passing app credentials and required scope (authorisation code flow)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE,
                                               client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               username=USERNAME))
