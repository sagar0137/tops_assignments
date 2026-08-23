#Create a Python class called Product with a method get_discount() that returns 0. Write a subclass called Electronics that 
# overrides get_discount() to return 10

# Parent class
class Product:
    def get_discount(self):
        return 0


# Child class
class Electronics(Product):
    def get_discount(self):
        return 10


# Create objects
product = Product()
electronics = Electronics()

# Display discounts
print("Product Discount:", product.get_discount(), "%")
print("Electronics Discount:", electronics.get_discount(), "%")
