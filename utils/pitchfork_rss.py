import sys
sys.path.append('../config/')

import feedparser
import re

# This file contains utility functions for parsing the
# Pitchfork RSS feeds and returning data structures
# that contain the RSS data

# URLs for Pitchfork RSS feeds
BASE_URL = 'http://pitchfork.com/rss/reviews/best/%s'
REISSUES_URL = BASE_URL % 'reissues/'
ALBUMS_URL = BASE_URL % 'albums/'
TRACKS_URL = BASE_URL % 'tracks/'


def get_best_new_tracks():
    """
    Parses the Pitchfork 'best new tracks' RSS feed
    and returns an array of track dicts (including
    track name and artist name)
    :return: list of tracks
    """
    # Regular expression for tracks
    pattern = re.compile(r'''(?P<artist>.+):\s  # Artist name
                             “(?P<track>.+)”.*  # Track name
                          ''', re.VERBOSE)

    # Parse the RSS feed
    feed = feedparser.parse(TRACKS_URL)
    print("Number of RSS posts: ", len(feed.entries))

    # Extract the best new tracks
    best_new_tracks = []
    for entry in feed.entries:
        match = pattern.match(entry.title)
        if match is None:
            print(f"No match for {entry.title}")
            print("-" * 50)
        else:
            artist = match.group('artist')
            track = match.group('track')
            print("Match found")
            print(f"Artist: {artist}")
            print(f"Track: {track}")
            print(match.groupdict())
            print("-" * 50)
            best_new_tracks.append(match.groupdict())

    return best_new_tracks


def get_best_new_albums(url=ALBUMS_URL):
    """
    Parses the Pitchfork 'best new albums' RSS feed
    and returns an array of album dicts (including
    album name and artist name)
    :return: list of albums
    """
    # Regular expression for albums
    pattern = re.compile(r'''(?P<artist>.+):\s  # Artist name
                             (?P<album>.+).*    # Album name
                          ''', re.VERBOSE)

    # Parse the RSS feed
    feed = feedparser.parse(url)
    print("Number of RSS posts: ", len(feed.entries))

    # Extract the best new albums
    best_new_albums = []
    for entry in feed.entries:
        match = pattern.match(entry.title)
        if match is None:
            print(f"No match for {entry.title}")
            print("-" * 50)
        else:
            artist = match.group('artist')
            album = match.group('album')
            print("Match found")
            print(f"Artist: {artist}")
            print(f"Album: {album}")
            print(match.groupdict())
            print("-" * 50)
            best_new_albums.append(match.groupdict())

    return best_new_albums


def get_best_new_reissues():
    """
    Parses the Pitchfork 'best new reissues' RSS feed
    and returns an array of reissue dicts (including
    reissue album name and artist name)
    :return: list of albums
    """
    return get_best_new_albums(url=REISSUES_URL)
