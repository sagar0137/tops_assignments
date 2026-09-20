#Write a function show_bonus(employee) that takes any object with a bonus() method and prints the result. Test it with two classes:
#  Influencer (bonus returns 2000) and BrandManager (bonus returns 5000), demonstrating polymorphism

# Class 1
class Influencer:
    def bonus(self):
        return 2000


# Class 2
class BrandManager:
    def bonus(self):
        return 5000


# Polymorphic function
def show_bonus(employee):
    print("Bonus: ₹", employee.bonus())


# Create objects
influencer = Influencer()
manager = BrandManager()

# Test the function
show_bonus(influencer)
show_bonus(manager)
