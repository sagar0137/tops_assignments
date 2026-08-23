#Create a recursive function count_likes(posts) that takes a nested dictionary representing Instagram posts and their replies 
# (each with a 'likes' key), and returns the total number of likes across all posts and replies.<br><br><em><strong>Hint:</strong>
#  Each reply can itself have more replies, so use recursion to sum likes at all levels.</em>

def count_likes(post):
    # Count likes of the current post
    total_likes = post["likes"]

    # Recursively count likes of all replies
    for reply in post.get("replies", []):
        total_likes += count_likes(reply)

    return total_likes


# Example Instagram post with nested replies
instagram_post = {
    "likes": 100,
    "replies": [
        {
            "likes": 25,
            "replies": [
                {
                    "likes": 10,
                    "replies": []
                },
                {
                    "likes": 15,
                    "replies": []
                }
            ]
        },
        {
            "likes": 40,
            "replies": [
                {
                    "likes": 20,
                    "replies": []
                }
            ]
        }
    ]
}

# Calculate total likes
total = count_likes(instagram_post)

print("Total Likes:", total)