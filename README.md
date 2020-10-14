# 🎧 Spoti Pitchfork
Spoti Pitchfork is a command-line interface that allows users to create playlists
including the best new tracks, albums and reissues as reviewed by [Pitchfork](https://pitchfork.com/).


## Features
* Parses the [Pitchfork RSS](https://pitchfork.com/rss/) feeds to get the names of the best reviewed tracks, albums, and reissues
* Uses the [Spotify API](https://developer.spotify.com/documentation/web-api/) to search for these items in the Spotify library
* Automatically generates playlists for these tracks, albums and/or reissues for a specific user

![alt text](best_new_reissues.png?raw=true "Pitchfork's Best New Reissues")

## Requirements
The CLI requires a [Spotify Developer](https://developer.spotify.com/) account and application with a Client ID and Client Secret

## Usage
1. Clone the repository
2. Install requirements
    ```bash
    $ pip install -r requirements.txt
    ```
3. Create a file called `spotify_client_credentials.py` in the `config` directory, with your Spotify application Client ID and Client Secret, and your Spotify username
    ```python
    # Spotify API Credentials
    CLIENT_ID     = <SPOTIFY_API_CLIENT_ID>
    CLIENT_SECRET = <SPOTIFY_API_CLIENT_SECRET>
    REDIRECT_URI  = 'http://google.com/'
    USERNAME      = <SPOTFIY_USERNAME>
    SCOPE         = 'user-library-read playlist-modify-public'
    ```

4. Run the script `create_playlists.py`
    ```bash
    $ python create_playlists.py --help

    usage: create_playlist.py [-h] [--tn TN] [--td TD] [--an AN] [--ad AD] [--rn RN] [--rd RD] [-t] [-a] [-r]

    Creates Spotify playlists for the user

    optional arguments:
    -h, --help      show this help message and exit
    --tn TN         Name of 'best new tracks' playlist
    --td TD         Description of 'best new tracks' playlist
    --an AN         Name of 'best new albums' playlist
    --ad AD         Description of 'best new albums' playlist
    --rn RN         Name of 'best new reissues' playlist
    --rd RD         Description of 'best new reissues' playlist
    -t, --tracks    Create playlist for 'best new tracks'
    -a, --albums    Create playlist for 'best new albums'
    -r, --reissues  Create playlist for 'best new reissues'
    ```

    **Note**: default playlist names will generated if not specified

5. Sample command to create best new tracks and reissues playlists:
    ```bash
    $ python create_playlists.py -tr
    ```


## License
MIT © Emmanuel Macario

## Attribution
Made by Emmanuel Macario