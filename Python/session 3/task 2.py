#Write a Python program that takes a user's input for the price of a Zomato order as a string, converts it to a float using
#  type casting,  adds 18% GST, and prints the final bill amount


order_price = input("Enter the price of order:-")
order_price = float(order_price)
gst = order_price*0.18
final_bill = order_price + gst

print("Original price of orde is:-" , order_price)
print("with gst the price is:-" , gst)
print("The Final ammout is :-" , final_bill)
print("thank you for order")