#Given two lists — one of food items and one of prices — use zip() to print each food item with its price like a Zomato menu
#  (e.g., 'Pizza - ₹250').


# List of food items
food_items = ["Pizza", "Burger", "Pasta", "Biryani", "Sandwich"]

# List of prices
prices = [250, 180, 220, 300, 150]

# Print menu using zip()
print(" Zomato Menu")
print("-" * 25)

for food, price in zip(food_items, prices):
    print(f"{food} - ₹{price}")