#Build a class called Playlist that has a private attribute _songs (a list of song names). Write methods to add a song, remove a
#  song, and get the current list of songs using proper encapsulation.

class Playlist:
    def __init__(self):
        self._songs = []   # Private attribute

    # Add a song
    def add_song(self, song):
        self._songs.append(song)
        print(f'"{song}" added to the playlist.')

    # Remove a song
    def remove_song(self, song):
        if song in self._songs:
            self._songs.remove(song)
            print(f'"{song}" removed from the playlist.')
        else:
            print(f'"{song}" not found in the playlist.')

    # Getter method
    def get_songs(self):
        return self._songs.copy()   # Return a copy to protect the original list


# Create a Playlist object
playlist = Playlist()

# Add songs
playlist.add_song("Shape of You")
playlist.add_song("Believer")
playlist.add_song("Perfect")

# Display current playlist
print("Current Playlist:", playlist.get_songs())

# Remove a song
playlist.remove_song("Believer")

# Display updated playlist
print("Updated Playlist:", playlist.get_songs())
