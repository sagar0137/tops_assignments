#Create a Python script that takes any product name string (e.g., 'Redmi Note 12 Pro') and prints the 
# name in all uppercase and all lowercase using the upper() and lower() methods.


# product name :-
mobile = "iphone 15 pro max"
owner_name = "Sagar Gupta"
address = "ahemdabad"

print("before changing in upper case and lower case")
print(f"The owner of this phone:-", mobile, "is" , owner_name , "and he is from:- ", address)

print("after changing in upper case ")

mobile=mobile.upper()
owner_name=owner_name.upper()
address=address.upper()
print(f"The owner of this phone:-", mobile, "is" , owner_name , "and he is from:- ", address)

print("after changing in lowercase:-")

mobile=mobile.lower()
owner_name=owner_name.lower()
address=address.lower()

print(f"The owner of this phone:-", mobile, "is" , owner_name , "and he is from:- ", address)