#Define a function called calculate_final_price(price, discount_rate) that returns the final price after applying the discount. 
#Test it with price 1200 and discount_rate 0.15.


def calculate_final_price(price,discount_rate):
    return price-(price*discount_rate)
price=calculate_final_price(1200,0.15)
print(price)