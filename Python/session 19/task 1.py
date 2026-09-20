#Define a Python class called Song with attributes title, artist, and duration (in seconds), and use the __init__()
#  constructor to initialize these values when creating an object

class song:
    def __init__(self, title, artist, duration):
        self.title=title
        self.artist=artist
        self.duration=duration
song1=song("tum hi ho","arijit singh",330)
song2=song("apna bana le","arijit singh",444)

print(song1.title)
print(song1.artist)
print(song1.duration)

