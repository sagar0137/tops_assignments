#Simulate a Zomato-style rating system: ask the user for number of reviews and total stars, then calculate average rating.
#  Use try-except to handle invalid (non-numeric) input and print an error message if input is not a number.
# <br><br><em><strong>Hint:</strong> Use input() and int() conversion inside a try block.</em>

try:
    # Taking input from the user
    reviews = int(input("Enter the number of reviews: "))
    total_stars = int(input("Enter the total stars received: "))

    # Check to avoid division by zero
    if reviews == 0:
        print("Number of reviews cannot be zero.")
    else:
        # Calculate average rating
        average_rating = total_stars / reviews
        print(f"Average Rating: {average_rating:.2f} ⭐")

except ValueError:
    print("Error: Please enter valid numeric values only.")
    