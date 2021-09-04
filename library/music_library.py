import os
import random
class MusicLibrary:

    def __init__(self, setting):
        self.setting = setting
        self.all_songs = None

    def get_songs_filepath(self, detected_qr_code):
        if self.is_music(detected_qr_code):
            return [self.get_song_filepath(detected_qr_code)]
        if self.is_playlist(detected_qr_code):
            return self.get_songs_from_playlist_filepath(detected_qr_code)
        return []

    def get_song_filepath(self, detected_qr_code):
        return os.path.join(self.setting.library_path, detected_qr_code)

    def get_songs_from_playlist_filepath(self, detected_qr_code):
        playlist_path = os.path.join(self.setting.playlist_path, detected_qr_code)
        songs_in_playlist = []
        if self.is_playlist(playlist_path):
            with open(playlist_path, "r", encoding='utf-8') as f:
                songs = f.readlines()
            songs_in_playlist = [self.get_song_filepath(song.replace("../", "").strip()) for song in songs]
        return songs_in_playlist

    def get_random_song_from_library(self):
        if self.all_songs is None:
            self.all_songs = []
            for root, _, files in os.walk(self.setting.library_path):
                for file in files:
                    if self.is_music(file):
                        self.all_songs.append(os.path.join(root, file))
        return random.choice(self.all_songs)

    @staticmethod
    def is_music(filepath):
        if filepath.endswith(".mp3"):
            return True
        return False

    @staticmethod
    def is_playlist(filepath):
        if filepath.endswith(".m3u"):
            return True
        return False