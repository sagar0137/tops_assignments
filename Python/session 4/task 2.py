#Write a function clean_brand_name(name) that removes leading/trailing spaces and replaces any hyphens '-' with a single space in 
# the input string. Test it with ' oneplus-Nord

# here we use two method to :
# to remove leading/trailing space :- we use strip() method 
# to replaces any hyphens with single space:- we use replace("-"," ") method 

def clean_brand_name(name):
    return name.strip().replace("-"," ")

brand= " OnePlus-Nord  "
cleaned_brand= clean_brand_name(brand)

print("Origial Brand Name :-", brand)
print("Cleaned Brand Name:-", cleaned_brand)

