#Use pathlib to check if a file called zomato_orders.json exists in your current directory, and print an appropriate message if it
#  is found or not.<br><br><em><strong>Hint:</strong> Use Path('zomato_orders.json').exists() from the pathlib module.</em>

from pathlib import Path

# Create a Path object
file_path = Path("zomato_orders.json")

# Check if the file exists
if file_path.exists():
    print(" File 'zomato_orders.json' exists.")
else:
    print(" File 'zomato_orders.json' does not exist.")
    