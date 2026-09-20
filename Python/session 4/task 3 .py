#Given the string 'Apple iPhone 14 Pro Max', use string slicing to extract and print only the brand name and the model
# (i.e., 'Apple' and 'iPhone 14 Pro Max') separately.<br><br><em><strong>Hint:</strong> Use split() to help find the split point,
#  then use slicing for the substrings.</em>


# here use use index number  method to extract the word for brand name and model name :-

phone= "Apple Iphone 14 Pro Max"

print(phone)

brand= phone[0:5]
print(brand)

model= phone[6:]
print(model)

print("The breand name of this phone ",phone , "is :-", brand , "and the model of this:-", model)