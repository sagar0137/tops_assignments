#You have a list of favorite song names: ['Kesariya', 'Believer', 'Shape of You', 'Blinding Lights', 'Excuses']. Use the enumerate()
#  function in a for loop to print each song with its playlist position (starting from 1).

favorite_song=['Kesariya', 'Believer', 'Shape of You', 'Blinding Lights', 'Excuses']

for position, song in enumerate(favorite_song , start=1):
    print(f"playlist position {position}: {song}")