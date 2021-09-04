import os
import inspect
import configparser

class Setting:

    INI_FILEPATH = os.path.join(os.path.dirname(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)), 'option.ini')
    PLAYLIST_FOLDER = 'Playlists'

    def __init__(self):
        self._library_path = None
        self._playlist_path = None

    @classmethod
    def set_library_path(cls, music_library_path):
        config = configparser.ConfigParser()
        config['DEFAULT'] = {}
        config['PATH'] = {}
        config['PATH']['MUSIC_LIBRARY'] = os.path.normpath(music_library_path)
        config['PATH']['PLAYLISTS'] = os.path.join(os.path.normpath(music_library_path), Setting.PLAYLIST_FOLDER)

        with open(Setting.INI_FILEPATH, 'w') as configfile:
            config.write(configfile)
        return Setting()

    @property
    def library_path(self):
        if self._library_path == None:
            config = configparser.ConfigParser()
            config.read(Setting.INI_FILEPATH)
            self._library_path = config['PATH']['MUSIC_LIBRARY']
        return self._library_path

    @property
    def playlist_path(self):
        if self._playlist_path == None:
            config = configparser.ConfigParser()
            config.read(Setting.INI_FILEPATH)
            self._playlist_path = config['PATH']['PLAYLISTS']
        return self._playlist_path

