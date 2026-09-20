#Create a Python class called Product with a private attribute _price. Initialize _price in the constructor and write a method 
# to display its value

class Product:
    def __init__(self, price):
        self._price = price   # Private attribute (by convention)

    def display_price(self):
        print("Product Price:", self._price)


# Create an object
product1 = Product(999)

# Display the price
product1.display_price()