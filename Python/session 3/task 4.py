#Build a function is_discount_applicable(order_amount) that takes a float and returns True if the amount is greater than 500,
#  otherwise False. Print the result for order amounts 450 and 750



# Function to check if discount is applicable


order_amount = int(input("Enter the amount to check discount:-"))

def is_discount_applicable(order_amount):
    return order_amount > 500

# Test the function
print("Order Amount: ", order_amount)
print("Discount Applicable:", is_discount_applicable(order_amount))

