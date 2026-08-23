#Given a JSON file named user_profile.json containing details like username, followers, and bio (similar to an Instagram profile),
#  use the json module to load the file and print the username and number of followers.

import json

# open and load JSON file 

with open("user_profile.json","r") as file:
    profile=json.load(file)

print("username:-",profile["username"])
print("followers:-",profile["followers"])
print("bio:-",profile["bio"])
