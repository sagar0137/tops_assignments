#Refactor your Song class so that it also tracks a play_count attribute (starting at 0), and add a method increment_play_count(self) 
# that increases play_count by 1 each time it's called. Show how you would use this to count how many times a user plays a song.
# <br><br><em><strong>Hint:</strong> Call increment_play_count() multiple times and print play_count to see the update.</em>

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.play_count = 0   # Starts at 0

    def play_preview(self):
        print(f"Playing 30-second preview of {self.title} by {self.artist}")

    def increment_play_count(self):
        self.play_count += 1


# Create a Song object
song1 = Song("Shape of You", "Ed Sheeran", 233)

# User plays the song three times
song1.increment_play_count()
song1.increment_play_count()
song1.increment_play_count()

# Show play count
print("Song Title:", song1.title)
print("Artist:", song1.artist)
print("Play Count:", song1.play_count)