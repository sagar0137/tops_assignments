#Write a function called calculate_cashback(amount, cashback_rate=0.05) that returns the cashback amount. Then, use it to calculate 
# cashback for a Zomato order of Rs. 500 with the default rate, and for a Flipkart order of Rs. 2000 with a 7% cashback

def calculate_cashback(amount, cashback_rate=0.05):
    cashback_amount=(amount*cashback_rate)
    return f"The returned cashback amount is :-  {cashback_amount}"
print("cashback for zomato:-")
print(calculate_cashback(500))
print("cashback for flipcart:-")
print(calculate_cashback(2000,0.07))
