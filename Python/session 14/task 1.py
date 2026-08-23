#1.Use open() in write mode to create a file called my_playlist.txt and write the names of 5 songs you listened to this week, 
# each on a new line.

with open("my_playlist.txt", "w") as file:
    file.write("Kesariya\n")
    file.write("Apna Bana Le\n")
    file.write("Heeriye\n")
    file.write("Tum Hi Ho\n")
    file.write("Saiyaara\n")

print("Playlist saved successfully!")