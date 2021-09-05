import json

from library.system_setting import Setting
from library import MusicLibrary, Spotify, spotify

class PlaylistMaker:
    @staticmethod
    def run():
        setting = Setting()
        print(setting.__dict__)
        spotify_api = Spotify(setting.client_id, setting.client_secret, setting.user)
        music_library = MusicLibrary(setting)
        music_library.get_random_song_from_library()
        playlists = spotify_api.user_playlists()
        for playlist in playlists:
            songs_in_plalist = spotify_api.get_tracks(playlist['playlist_id'])
            for song in songs_in_plalist:
                print(song)




        with open("my_json.json", "w", encoding='utf8') as file:
            json.dump(songs_in_plalist, file, indent=4, sort_keys=True, ensure_ascii=False)
            #
            #


if __name__ == '__main__':
    PlaylistMaker.run()



