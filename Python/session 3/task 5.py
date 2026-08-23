#You received a dataset of ratings as strings from Spotify: ['4.5', '3.0', '5', '4.2']. Use type casting to convert these to floats,
#then find and print the highest rating.<br><br><em><strong>Hint:</strong>
# Use the float() function inside a loop or list comprehension.</em>


# rating data base from spotify :-
ratings = ['4.5','3.0','5','4.2']
float_rating = [float(rating) for rating in ratings ]
print(float_rating)
print(ratings)

print(type(ratings))
print(type(float_rating))
for x in float_rating:
    print(x)


print(f"the highest rating in above rating is :- " , max(float_rating))
