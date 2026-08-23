#Given a list of strings representing product prices from Flipkart, like ['199.99', '299.50', '150'], 
# convert all to floats and calculate the total cart value.

price_of_the_items_of_flipkart = [234.99,443,543,434,344,224.99,233,779]
prices= price_of_the_items_of_flipkart
float_price = [float(price) for price in prices]

total_cart_value= sum(float_price)

total = total_cart_value

print("The original price of the items is:-" , prices)
print("After changing price in float is:-" , float_price)
print("Total value of the cart is :-" , total)


