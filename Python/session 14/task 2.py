#2.Read the my_playlist.txt file you created and print each song name in uppercase using Python file handling.
# Read the file and print each song name in uppercase

with open("my_playlist.txt", "r") as file:
    for song in file:
        print(song.strip().upper())