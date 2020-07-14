import feedparser
import re

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
            print("---" * 25)
        else:
            artist = match.group('artist')
            track = match.group('track')
            print("Match found")
            print(f"Artist: {artist}")
            print(f"Track: {track}")
            print(match.groupdict())
            print("---" * 25)
            best_new_tracks.append(match.groupdict())

    return best_new_tracks


def get_best_new_albums():
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
    feed = feedparser.parse(ALBUMS_URL)
    print("Number of RSS posts: ", len(feed.entries))

    # Extract the best new albums
    best_new_albums = []
    for entry in feed.entries:
        match = pattern.match(entry.title)
        if match is None:
            print(f"No match for {entry.title}")
            print("---" * 25)
        else:
            artist = match.group('artist')
            album = match.group('album')
            print("Match found")
            print(f"Artist: {artist}")
            print(f"Album: {album}")
            print(match.groupdict())
            print("---" * 25)
            best_new_albums.append(match.groupdict())

    return best_new_albums


def get_best_new_reissues():

    pass


if __name__ == "__main__":
    s = get_best_new_albums()
    print(s)
