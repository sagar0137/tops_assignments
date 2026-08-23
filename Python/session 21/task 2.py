#Build a class FoodOrder with a method calculate_total() that returns the base price. Create a subclass ZomatoOrder that overrides 
# calculate_total() to add a 5% delivery charge

# Parent class
class FoodOrder:
    def __init__(self, base_price):
        self.base_price = base_price

    def calculate_total(self):
        return self.base_price


# Child class
class ZomatoOrder(FoodOrder):
    def calculate_total(self):
        delivery_charge = self.base_price * 0.05  # 5% delivery charge
        return self.base_price + delivery_charge


# Create objects
order1 = FoodOrder(500)
order2 = ZomatoOrder(500)

# Display totals
print("Food Order Total: ₹", order1.calculate_total())
print("Zomato Order Total: ₹", order2.calculate_total())
