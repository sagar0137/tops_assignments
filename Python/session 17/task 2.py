#Write a script that lists all files in your current directory using the os module, and prints only those files with a .jpg or 
# .png extension.<br><br><em><strong>Hint:</strong> Use os.listdir() and string methods to filter file names.</em


import os

# Get all files and folders in the current directory
items = os.listdir()

print("Image files in the current directory:")

# Loop through each item
for item in items:
    # Check if the item is a file and has .jpg or .png extension
    if os.path.isfile(item) and item.lower().endswith((".jpg", ".png")):
        print(item)
        