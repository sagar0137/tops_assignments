#Write a generator function called insta_posts_generator(posts) that takes a list of Instagram post captions and yields one 
# caption at a time. Use next() to get and print the next post caption each time until all captions are printed.<br><br><em>
#<strong>Hint:</strong> Use the yield keyword inside your function and handle StopIteration when all posts are done.</em>


# Generator function
def insta_posts_generator(posts):
    for post in posts:
        yield post

# List of Instagram post captions
posts = [
    "Chasing sunsets!",
    "Coffee first, then everything else.",
    "Beach vibes only.",
    "Reading my favorite book.",
    "Weekend fun with friends!"
]

# Create generator object
post_generator = insta_posts_generator(posts)

# Print captions one by one using next()
try:
    while True:
        print(next(post_generator))
except StopIteration:
    print("No more Instagram posts!")