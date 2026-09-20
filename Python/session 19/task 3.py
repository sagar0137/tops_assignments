#Add a method play_preview(self) to your Song class that prints 'Playing 30-second preview of [title] by [artist]'. 
# Call this method for your Song object.
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play_preview(self):
        print(f"Playing 30-second preview of {self.title} by {self.artist}")


# Create a Song object
song1 = Song("keshariya", "arijit singh", 233)

# Call the play_preview() method
song1.play_preview()