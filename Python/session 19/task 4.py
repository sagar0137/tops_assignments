#Create a class called FoodOrder with attributes restaurant_name, items (a list), and total_price. Add a method add_item(self, item,
#  price) that adds the item to the items list and updates total_price. Demonstrate by creating a FoodOrder object and adding two
#  items like you would on Zomato.


class FoodOrder:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.items = []
        self.total_price = 0

    def add_item(self, item, price):
        self.items.append(item)
        self.total_price += price
        print(f"{item} added successfully!")

    def show_order(self):
        print("\n----- Food Order -----")
        print("Restaurant:", self.restaurant_name)
        print("Items:", self.items)
        print("Total Price: ₹", self.total_price)


# Create a FoodOrder object
order = FoodOrder("Zomato - Pizza Hut")

# Add two items
order.add_item("Veg Pizza", 299)
order.add_item("Garlic Bread", 149)

# Display the order
order.show_order()