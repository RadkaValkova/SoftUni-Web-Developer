# from spoopify_08.project.album import Album
# from spoopify_08.project.song import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f'Band {self.name} already has {album.name} in their library.'
        else:
            self.albums.append(album)
            return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name:str):
        current_album = [el for el in self.albums if el.name == album_name]
        if current_album:
            album = current_album[0]
            if album.published:
                return f'Album has been published. It cannot be removed.'
            if album not in self.albums:
                return f'Album {album_name} is not found.'
            if album in self.albums:
                self.albums.remove(album)
                return f'Album {album_name} has been removed.'
        return f'Album {album_name} is not found.'

    def details(self):
        result = f'Band {self.name}\n'
        for el in self.albums:
            result += f'{el.details()}\n'
        return result


# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())


