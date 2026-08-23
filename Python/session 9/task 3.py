#Build a function called format_coupon_message(username, discount=10) that returns a string like 'Hi Rahul, you get 10% off!' 
# If no discount is given, use 10% by default. Test it for two users: one with a custom discount, one with the default

def format_coupan_message(username,discount=10):
    return f"Hi {username},you get {discount}% off!!"
 # testing with custom discount
print("for custom discount:-")
print(format_coupan_message("Rahul",20))

print("for default discont:-")
print(format_coupan_message("Sagar"))