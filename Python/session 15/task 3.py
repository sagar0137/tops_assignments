#Create a function get_playlist_duration(songs) that takes a list of song durations (in seconds) and returns the total duration in 
# minutes. Raise a custom exception InvalidDurationError if any duration in the list is negative.<br><br><em><strong>Hint:</strong>
#  Define your own exception class by subclassing Exception.</em>

# Custom Exception
class InvalidDurationError(Exception):
    """Raised when a song duration is negative."""
    pass


def get_playlist_duration(songs):
    total_seconds = 0

    for duration in songs:
        if duration < 0:
            raise InvalidDurationError(
                f"Invalid song duration: {duration} seconds. Duration cannot be negative."
            )
        total_seconds += duration

    # Convert total seconds to minutes
    total_minutes = total_seconds / 60
    return total_minutes


# Example 1: Valid playlist
try:
    playlist = [210, 180, 240, 150]
    print(f"Total Playlist Duration: {get_playlist_duration(playlist):.2f} minutes")
except InvalidDurationError as e:
    print(e)


# Example 2: Invalid playlist
try:
    playlist = [210, -180, 240]
    print(f"Total Playlist Duration: {get_playlist_duration(playlist):.2f} minutes")
except InvalidDurationError as e:
    print("Error:", e)
    