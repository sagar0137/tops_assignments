#Create a Python program that accepts a date in 'YYYY-MM-DD' format from the user and displays the day of the week using the
#  datetime module
from datetime import datetime

# Get date input from the user
date_input = input("Enter a date (YYYY-MM-DD): ")

try:
    # Convert string to datetime object
    date_obj = datetime.strptime(date_input, "%Y-%m-%d")

    # Get the day of the week
    day_name = date_obj.strftime("%A")

    # Display the result
    print(f"The day of the week is: {day_name}")

except ValueError:
    print("Invalid date format! Please enter the date in YYYY-MM-DD format.")
