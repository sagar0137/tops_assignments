#Build a Python script that asks the user for their Zomato order total and prints 'Apply Free Delivery' if total is above 299,
#  'Add more items for free delivery' if between 200 and 299, else 'Delivery charges apply'


total=int(input("Enter the total "))
print("your have order of ammount",total)
if total >299:
    print("Apply for free Delivery")
elif total in range(200,299):
    print('Add more items for free delivery')
else:
    print('Delivery charge will apply')
