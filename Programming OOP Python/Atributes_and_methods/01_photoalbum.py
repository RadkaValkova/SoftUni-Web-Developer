class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.page = 0
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return PhotoAlbum(photos_count // 4)

    def add_photo(self, label: str):
        try:
            if len(self.photos[self.page]) == 4:
                self.page += 1
        except:
            return 'No more free spots'
        if self.page >= self.pages:
            return 'No more free spots'
        self.photos[self.page].append(label)
        return f'{label} photo added successfully on page {self.page + 1} slot {len(self.photos[self.page])}'

    def display(self):
        result = ''
        for page in self.photos:
            result += f'{"-" * 11}\n'
            result += ' '.join('[]' for _ in page) + '\n'
        result += '-' * 11 + '\n'
        return result


# album = PhotoAlbum(5)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())

album = PhotoAlbum(3)
for _ in range(8):
    album.add_photo("asdf")
result = album.display()
