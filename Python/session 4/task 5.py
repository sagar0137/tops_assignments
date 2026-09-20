#Suppose you have a list of messo product names: [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']. Write code to clean 
# each name (remove spaces, replace hyphens with spaces, and make the brand title case) and print the cleaned list.
# <br><br><em><strong>Constraint:</strong> Use at least three string methods from this session.</em>

# here we use three string method for cleaning the data thats are- strip, replace, and title method 

product_name= [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']
x=product_name[0]
y=product_name[1]
z=product_name[2]

# cleaning the product:-
print("here are the cleaned data:-")

clean_x= x.strip().replace("-"," ").title()
clean_y= y.strip().replace("-"," ").title()
clean_z= z.strip().replace("-"," ").title()
print(clean_x)
print(clean_y)
print(clean_z)

