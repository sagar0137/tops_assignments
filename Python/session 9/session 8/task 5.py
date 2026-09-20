#Write a for loop that goes through a list of Instagram follower counts [120, 1500, 23000, 800, 45000] and prints 'Micro', 
# 'Influencer', or 'Celebrity' for each, based on the following: Micro (<1000), Influencer (1000-10000), Celebrity (>10000).
# <br><br><em><strong>Hint:</strong> Use if-elif-else inside the loop to check the follower count range.</em>
    

followers=[120, 1500, 23000, 800, 45000]
for follower in followers:
    if follower <1000:
        print("this person have ",follower,"follower so he is in :-Micro category ")
    elif follower<10000:
        print("this person have :-",follower, "follower so he is in :-Influencer category ")
    else:
        print("this person have:-",follower, "follower so he is in :-Celebrity category ")
