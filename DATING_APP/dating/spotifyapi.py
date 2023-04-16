import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

def getUserSpotifyInfo():

    scope = "user-library-read"

    
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id='9f19e6e4332c4b9494f8fe6adcf0360a', client_secret='4d689b157da34bb5a9bb660b87c70c99', redirect_uri='http://127.0.0.1:8000'))

    results = sp.current_user_saved_tracks()
    artist_uris = []
    artists = []
    popularity = []
    durations = []
    genres = []
    for idx, item in enumerate(results['items']):
        track = item['track']
        durations.append(track['duration_ms'])
        popularity.append(track['popularity'])
        for artist in track['artists']:
            artist_uris.append(artist['uri'])
            artists.append(artist['name'])

    for artist in artist_uris:
        results = sp.artist(artist)['genres']
        genres = genres + results

    return {"artists": artists, "genres": genres, "popularities": popularity, "durations": durations}

