#Given two sets: set1 contains the names of restaurants you have ordered from on Zomato, and set2 contains the names of restaurants
#you have ordered from on Swiggy, find and print the union and intersection of these sets.<br><br><em><strong>Hint:</strong>
#Use the union() and intersection() methods of Python sets.</em

zomato_order={"harikripa hotel","hotel sharda","hotel mountain view","hotel sitara"}
swiggy_order={"azanta hotel","taj hotel","hotel mountain view","hotel sitara"}

result=zomato_order.union(swiggy_order)
print("union of restaurants are:-", result)
inter= zomato_order.intersection(swiggy_order)
print("Intersection of the restaurants are:-", inter)


# here union method is used to merge two sets 
# and intersection method is used to get the common value present in both sets
