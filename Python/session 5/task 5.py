#Given two scenarios — storing a user's favorite genres (which may change) and storing a fixed set of IRCTC train classes
#  ('Sleeper', 'AC 3 Tier', 'AC 2 Tier') — choose whether to use a list or tuple for each. Write one sentence explaining 
# your choice for both.


favorite_genres=["Pop","Rock","Hip-Hop","Classical","Bollywood"]
# here we use list which may change 

train_class= ('Sleeper', 'AC 3 Tier', 'AC 2 Tier')
# here we choose tuple which is fix in trains 

print("Users fevorite genres are:-", favorite_genres)
print("Trains classes are:-", train_class)


# for the users genres we use list which is mutable and could be change according to the users mindset
# for the train class we use tuple which is immutable because train classes could not be change 