#Given a list of order amounts from a Zomato cart [120, 340, 560, 80], use reduce() from functools to calculate the total 
# bill amount

from functools import reduce
zomato_cart=[120,340,560,80]
reudsed=reduce(lambda x,y: x+y, zomato_cart)
print("total bill amount:-")
print(reudsed)
