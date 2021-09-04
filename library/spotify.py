from requests import get, post
from socket import gethostbyname, gethostname
from base64 import b64encode
import webbrowser as spotifyweb

class Spotify():
    def __init__(self, token=None, user_id=None):
        self.token = token
        self.user_id = user_id

    def get_token(self, CLIENT_ID, CLIENT_SECRET):
        try:
            data = {
                'grant_type': 'client_credentials'
            }
            header = {
                'Authorization' : 'Basic {}'.format(b64encode(str(f"{CLIENT_ID}:{CLIENT_SECRET}").encode()).decode())
            }
            source = post("https://accounts.spotify.com/api/token", data=data, headers=header).json()
            return source['access_token']

        except Exception as __error__:
            if f"{gethostbyname(gethostname())}" == "127.0.0.1":
                return "You're Offline."
            else:
                return f"Please Report the issue to developer, 'Error : {__error__}'"

    def user_playlists(self):
        try:
            json_response = get(f"https://api.spotify.com/v1/users/{self.user_id}/playlists",
            headers={
                "Content-Type":"application/json",
                "Authorization":f"Bearer {self.token}"
                }
            ).json()

            source = json_response['items']

            print(json_response['items'])
            return [dict(
                playlist_name = playlist['name'],
                playlist_description = playlist['description'],
                playlist_image = playlist['images'][0]['url'],
                playlist_owner = playlist['owner']['display_name']
            ) for playlist in source]

        except Exception as __error__:
            if f"{gethostbyname(gethostname())}" == "127.0.0.1":
                return "You're Offline."
            else:
                return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"

    def get_tracks(self, playlist_id=""):
        try:
            json_response = get(f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks",
            headers={
                "Content-Type":"application/json",
                "Authorization":f"Bearer {self.token}"
                }
            ).json()

            source = json_response['items']

            return [{
                "song_name": track['track']['name'],
                "album": track['track']['album']['name'],
                "artist": track['track']['artists'][0]['name']
            } for track in source]

        except Exception as __error__:
            if f"{gethostbyname(gethostname())}" == "127.0.0.1":
                return "You're Offline."
            else:
                return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"
