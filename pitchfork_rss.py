import lxml
import feedparser
import re

# URLs for Pitchfork RSS feeds
BASE_URL = 'http://pitchfork.com/rss/reviews/best/%s'
REISSUES_URL = BASE_URL % 'reissues/'
ALBUMS_URL = BASE_URL % 'albums/'
TRACKS_URL = BASE_URL % 'tracks/'


def main():
    print(REISSUES_URL)
    print(ALBUMS_URL)
    print(TRACKS_URL)

    """
    pattern = re.compile(r"(?P<artist>.+):\s # Track name
                             "(?P<track>.+)"   # Artist name
                          ", re.VERBOSE)
    """

    pattern = re.compile(r'(?P<artist>.+):\s“(?P<track>.+)”.*')

    pitchfork_feed = feedparser.parse(TRACKS_URL)
    print("Number of RSS posts: ", len(pitchfork_feed.entries))
    for entry in pitchfork_feed.entries:
        print(entry.title)

        match = pattern.match(entry.title)
        if match is None:
            print(f"No match for {entry.title}")
            print("---"*25)
        else:
            artist = match.group('artist')
            track = match.group('track')
            print("Match found")
            print(f"Artist: {artist}")
            print(f"Track: {track}")
            print(match.groupdict())
            print("---" * 25)


if __name__ == "__main__":
    main()