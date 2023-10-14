import os
from secrets import choice
from unicodedata import name
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import urllib.request

# Set up Spotify API credentials
client_id = 'your-client-id-goes-here'
client_secret = 'your-client-secret-goes-here'
redirect_uri = 'https://m.youtube.com'
scope = 'playlist-modify-public,user-library-read'

# Authenticate with Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))


def create_playlist():
    # Get playlist name and file path from user
    playlist_name = input("Enter the name of your new playlist: ")
    file_path = input('enter your file path')

    # Create new playlist
    user_id = sp.me()['id']
    sp.user_playlist_create(user_id, playlist_name)
    playlist_id = sp.user_playlists(user_id)['items'][0]['id']

    # Add songs from file to playlist
    with open(file_path, 'r') as f:
        song_names = f.readlines()
    for song_name in song_names:
        search_results = sp.search(song_name.strip(), type='track', limit=1)
        if search_results['tracks']['items']:
            track_uri = search_results['tracks']['items'][0]['uri']
            sp.playlist_add_items(playlist_id, [track_uri])

    # Ask user if they want to add more songs
    while True:
        add_more = input(
            "Do you want to add more songs to the playlist? (y/n): ")
        if add_more.lower() == 'y':
            song_name = input("Enter the name of the song: ")
            search_results = sp.search(song_name, type='track', limit=1)
            if search_results['tracks']['items']:
                track_uri = search_results['tracks']['items'][0]['uri']
                sp.playlist_add_items(playlist_id, [track_uri])
        elif add_more.lower() == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    print("Playlist created!")


# def download():
    # Get playlist ID from URL
    playlist_id = input('Enter the playlist id:')

    # Get all the tracks in the playlist
    tracks = sp.playlist_tracks(playlist_id)

    # Download each track and save to user's music directory
    music_directory = os.path.expanduser("~/Music")

    for track in tracks['items']:
        # Get the track details
        track_name = track['track']['name']
        track_artist = track['track']['artists'][0]['name']
        track_album = track['track']['album']['name']
        track_id = track['track']['id']
        track_url = sp.track(track_id)['external_urls']

        # Create filename
        filename = f"{track_name} - {track_artist} - {track_album}.mp3"
        filepath = os.path.join(music_directory, filename)

        # Download the track
        if track_url:
            urllib.request.urlretrieve(track_url, filepath)
            print(f"Downloaded {filename}")
        else:
            print(f"Could not download {filename}")

    print("All songs downloaded!")


def main():
    print("Choose an option:")
    print("Create or download playlist from list of songs")
    print('// Download function still in progress...')
    choice = str(input('Enter download or create : '))

    # if choice == 'download':
    #     download()
    if choice == 'create':
        create_playlist()
    else:
        print('Alright, catch you later')


main()


# import os
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# import urllib.request

# # Set up Spotify API credentials
# client_id = 'your-client-id'
# client_secret = 'your-client-secret'
# redirect_uri = 'your-redirect-uri'
# scope = 'user-library-read'

# # Authenticate with Spotify API
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
#                                                client_secret=client_secret,
#                                                redirect_uri=redirect_uri,
#                                                scope=scope))
