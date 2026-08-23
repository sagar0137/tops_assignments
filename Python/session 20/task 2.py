# Add getter and setter methods for the _price attribute in your Product class to safely access and update the price. Make sure
#  the setter prevents setting a negative price.<br><br><em><strong>Hint:</strong> Raise a ValueError if the new price is less than 
# zero.</em>
    
class Product:
    def __init__(self, price):
        self._price = price

    # Getter method
    def get_price(self):
        return self._price

    # Setter method
    def set_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self._price = new_price


# Create a Product object
product = Product(999)

# Get the current price
print("Current Price:", product.get_price())

# Update the price
product.set_price(1200)
print("Updated Price:", product.get_price())

# Try to set a negative price
try:
    product.set_price(-500)
except ValueError as e:
    print("Error:", e)