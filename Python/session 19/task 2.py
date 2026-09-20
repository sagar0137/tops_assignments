#Create an object of the Song class for your favorite track from Spotify, and print out its title and artist using object attributes.
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