import argparse
from datetime import date
from config.auth import sp
from pitchfork_rss import get_best_new_tracks, get_best_new_albums, get_best_new_reissues
from search import search_for_tracks, search_for_albums, get_tracks_for_albums


def create_best_new_tracks_playlist(user_id, args):
    """
    Creates a 'best new tracks' playlist for a user
    :param user_id: authenticated user ID
    :param args: parsed command-line arguments
    :return: None
    """
    playlist_id = sp.user_playlist_create(user_id, args.tn, True, args.td)['id']
    best_new_tracks = get_best_new_tracks()
    track_ids = search_for_tracks(best_new_tracks)
    sp.user_playlist_add_tracks(user_id, playlist_id, track_ids)


def create_best_new_albums_playlist(user_id, args):
    """
    Creates a 'best new albums' playlist for a user
    :param user_id: authenticated user ID
    :param args: parsed command-line arguments
    :return: None
    """
    playlist_id = sp.user_playlist_create(user_id, args.an, True, args.ad)['id']
    best_new_albums = get_best_new_albums()
    album_ids = search_for_albums(best_new_albums)
    track_ids = get_tracks_for_albums(album_ids)
    add_tracks_to_playlist(user_id, playlist_id, track_ids)


def create_best_new_reissues_playlist(user_id, args):
    """
    Creates a 'best new reissues' playlist for a user
    :param user_id: authenticated user ID
    :param args: parsed command-line arguments
    :return: None
    """
    playlist_id = sp.user_playlist_create(user_id, args.rn, description=args.rd)['id']
    best_new_reissues = get_best_new_reissues()
    album_ids = search_for_albums(best_new_reissues)
    track_ids = get_tracks_for_albums(album_ids)
    add_tracks_to_playlist(user_id, playlist_id, track_ids)


def add_tracks_to_playlist(user_id, playlist_id, track_ids):
    """
    Adds tracks to the currently authenticated user's playlist
    :param user_id: authenticated user ID
    :param playlist_id: Spotify playlist ID
    :param track_ids: list of Spotify track IDs
    :return: None
    """
    # Partition track IDs into sub-lists of length 100 or less
    # Needed because the endpoint only allows addition of max
    # 100 tracks to a playlist for each single request
    track_ids_chunks = [track_ids[i: i + 100] for i in range(0, len(track_ids), 100)]
    for track_ids_chunk in track_ids_chunks:
        sp.user_playlist_add_tracks(user_id, playlist_id, track_ids_chunk)


def get_args():
    # Get current date
    today = date.today()
    date_str = today.strftime("%B %d, %Y")

    # Set arguments and options
    parser = argparse.ArgumentParser(description='Creates Spotify playlists for the user')
    parser.add_argument('--tn', required=False, default="Pitchfork 'Best New Tracks'",
                        help="Name of 'best new tracks' playlist")
    parser.add_argument('--td', required=False, default=f'The best new tracks as of {date_str}',
                        help="Description of 'best new tracks' playlist")
    parser.add_argument('--an', required=False, default="Pitchfork 'Best New Albums'",
                        help="Name of 'best new albums' playlist")
    parser.add_argument('--ad', required=False, default=f'The best new albums as of {date_str}',
                        help="Description of 'best new albums' playlist")
    parser.add_argument('--rn', required=False, default="Pitchfork 'Best New Reissues'",
                        help="Name of 'best new reissues' playlist")
    parser.add_argument('--rd', required=False, default=f'The best new reissues as of {date_str}',
                        help="Description of 'best new reissues' playlist")
    parser.add_argument('-t', '--tracks', action="store_true",
                        help="Create playlist for 'best new tracks'")
    parser.add_argument('-a', '--albums', action="store_true",
                        help="Create playlist for 'best new albums'")
    parser.add_argument('-r', '--reissues', action="store_true",
                        help="Create playlist for 'best new reissues'")
    return parser.parse_args()


def main():
    """
    Main program, responsible for parsing command-line
    arguments and facilitating the creation of playlists
    for the authenticated user
    :return: None
    """
    # Get the current authenticated user's ID
    user_id = sp.me()['id']
    # Parse the command-line arguments
    args = get_args()
    if args.tracks:
        create_best_new_tracks_playlist(user_id, args)
    if args.albums:
        create_best_new_albums_playlist(user_id, args)
    if args.reissues:
        create_best_new_reissues_playlist(user_id, args)


if __name__ == '__main__':
    main()
