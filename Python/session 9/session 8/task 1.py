#Create a Python list called order_amounts with the values [120, 250, 90, 310, 150]. Use a for loop to calculate and print
#  the total order value


order_amounts= [120,250,90,310,150]
total = 0
for num in order_amounts:
    total=total+num
print("total of the list is :-", total)