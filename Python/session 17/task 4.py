#Build a simple custom module named insta_utils.py with a function format_follower_count(n) that returns '1.5K' for 1500 and '2.3M'
#  for 2300000. Import and use this function in another script to display formatted counts for 3 sample numbers.


from insta_utils import format_follower_count

# Sample follower counts
followers = [850, 1500, 2300000]

print("Instagram Follower Counts")
print("-" * 30)

for count in followers:
    print(f"{count} -> {format_follower_count(count)}")