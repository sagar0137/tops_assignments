#Given a messy text copied from a Zomato review containing multiple emails, use re.findall() to extract all valid email addresses 
# and print them as a list

import re

# Messy Zomato review text
text = """
Great food! Contact us at support@zomato.com.
For complaints, email help123@gmail.com.
You can also reach manager.food@restaurant.co.in.
Ignore invalid emails like user@com or @gmail.com.
"""

# Regular expression for valid email addresses
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Find all email addresses
emails = re.findall(pattern, text)

# Print the list of emails
print(emails)
