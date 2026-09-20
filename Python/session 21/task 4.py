#Given this code: class User: def get_status(self): return 'active' class PremiumUser(User): pass. Update PremiumUser to override
#  get_status() so it returns 'premium'. Then, create one User and one PremiumUser and print their statuses.
# <br><br><em><strong>Hint:</strong> Use the same method name in both classes to override.</em>

# Parent class
class User:
    def get_status(self):
        return "active"


# Child class
class PremiumUser(User):
    def get_status(self):
        return "premium"


# Create objects
user = User()
premium_user = PremiumUser()

# Print statuses
print("User Status:", user.get_status())
print("Premium User Status:", premium_user.get_status())
