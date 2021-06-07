# from spoopify_08.project.song import Song


class Album:
    def __init__(self, name, songs=None):
        self.name = name
        if songs is None:
            self.songs = []
        elif not isinstance(songs, list):
            self.songs = []
            self.songs.append(songs)
        else:
            self.songs = songs
        self.published = False

    def add_song(self, song):
        if song.single:
            return f'Cannot add {song.name}. It\'s a single'
        if self.published:
            return 'Cannot add songs. Album is published.'
        if song in self.songs:
            return 'Song is already in the album.'
        if song not in self.songs:
            self.songs.append(song)
            return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        if song_name not in [el.name for el in self.songs]:
            return 'Song is not in the album.'
        if self.published:
            return 'Cannot remove songs. Album is published.'
        current_song = [el for el in self.songs if el.name == song_name]
        if current_song[0] in self.songs:
            self.songs.remove(current_song[0])
            return f'Removed song {song_name} from album {self.name}.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'
        else:
            self.published = True
            return f'Album {self.name} has been published.'

    def details(self):
        result = f'Album {self.name}\n'
        for el in self.songs:
            result += f'== {el.get_info()}\n'
        return result

