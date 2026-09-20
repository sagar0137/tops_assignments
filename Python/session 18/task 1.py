#Use re.findall() to extract all valid Indian phone numbers (10 digits, starting with 7, 8, or 9) from a given text string that
#  contains random numbers, prices, and phone numbers like those seen in OLX or WhatsApp chats.

import re

# Sample text containing random numbers, prices, and phone numbers
text = """
OLX Seller: Call me at 9876543210.
Backup number: 8123456789
Price: ₹25,000
Order ID: 123456789012
WhatsApp: 9123456780
Random number: 6543219870
Another contact: 7890123456
PIN Code: 110001
"""

# Regular expression for valid Indian mobile numbers
pattern = r'\b[789]\d{9}\b'

# Find all matching phone numbers
phone_numbers = re.findall(pattern, text)

# Print the results
print("Valid Indian Phone Numbers:")
for number in phone_numbers:
    print(number)