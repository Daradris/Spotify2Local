import os
import inspect
import configparser

class Setting:

    INI_FILEPATH = os.path.join(os.path.dirname(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)), 'option.ini')

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(Setting.INI_FILEPATH)

        self.library_path = config['PATH']['MUSIC_LIBRARY']
        self.playlist_path = config['PATH']['PLAYLISTS']
        self.client_id = config['SPOTIFY']['CLIENT_ID']
        self.client_secret = config['SPOTIFY']['CLIENT_SECRET']
        self.user = config['SPOTIFY']['USER']
