#Build a recursive function sum_playlist_durations(durations) that takes a list of song durations (in seconds) and returns the total
#  duration, similar to how Spotify totals a playlist.

def sum_playlist_durations(durations):
    # Base case
    if len(durations) == 0:
        return 0

    # Recursive case
    return durations[0] + sum_playlist_durations(durations[1:])


# Example playlist durations (in seconds)
playlist = [210, 180, 240, 150]

# Calculate total duration
total = sum_playlist_durations(playlist)


print("Song Durations:", playlist)
print("Total Duration:", total, "seconds")