#Use iter() and next() to manually loop through a list of 5 trending movies from BookMyShow and print each movie name one by one


# List of 5 trending movies
movies = [
    "Coolie",
    "War 2",
    "Saiyaara",
    "The Fantastic Four: First Steps",
    "Superman"
]

# Create an iterator
movie_iterator = iter(movies)

# Manually access each element using next()
print(next(movie_iterator))
print(next(movie_iterator))
print(next(movie_iterator))
print(next(movie_iterator))
print(next(movie_iterator))
