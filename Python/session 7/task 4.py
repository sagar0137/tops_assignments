#Write a Python program using nested if statements: take a user's entered Flipkart cart value and payment method 
# ('UPI', 'Card', 'Cash'). If the cart value is above 1000 and payment method is 'UPI', print 'Eligible for 10% cashback'; 
# if above 1000 and payment is not 'UPI', print 'Eligible for 5% cashback'; else print 'No cashback'

cart_value=int(input("Enter the cart value:-"))
pay_method=input("Choose payment method in-(UPI/card/cash):-" )

if cart_value>1000:
    if pay_method=="UPI":
        print("Eligible for 10% cashback")
    else:
        print("Eligible for 5% cashback")
else:
    print("No Cashback")