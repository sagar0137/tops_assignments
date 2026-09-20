#Simulate a Flipkart shopping cart: start with a list cart_items containing 't-shirt', 'shoes'. Use extend() to add 
# ['jeans', 'cap'] to the cart, then print the final list of items

# use of extend method to merge two list :-

cart_list= ['t-shirt','shoes']
print("Before use of extend method:-")
print("The original list is:-", cart_list)

print("After using extend method :-")

to_extend= ['Jeans','caps']

cart_list.extend(to_extend) 

print("The new list is:-" , cart_list)
