import math

class PhotoAlbum:
    PHOTOS_PER_PAGE  = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> 'PhotoAlbum':
        return cls(math.ceil(photos_count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label: str) -> str:

        for index, page in enumerate(self.photos):
            if len(page) < self.PHOTOS_PER_PAGE:
                page.append(label)

                return f"{label} photo added successfully on page {index + 1} slot {len(page)}"

        return "No more free slots"

    def display(self) -> str:
        separator = '-' * 11 + '\n'
        result = separator

        for page in self.photos:
            result += ' '.join(['[]' for _ in page]) + '\n'
            result += separator

        return result.strip()


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
