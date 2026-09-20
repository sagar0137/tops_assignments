#Create a playlist of 6 songs (as a list of strings) and use enumerate() to print each song with its position like Spotify's
#  tracklist (e.g., '1. Kesariya')


# Playlist of 6 songs
playlist = [
    "Kesariya",
    "Apna Bana Le",
    "Tum Hi Ho",
    "Heeriye",
    "Raataan Lambiyan",
    "Shayad"
]

# Print songs with their track number
for position, song in enumerate(playlist, start=1):
    print(f"{position}. {song}")

    