#Use re.sub() to mask all but the last 4 digits of any phone number in a string (e.g., replace 9876543210 with ******3210) like 
# Paytm does for privacy.<br><br><em><strong>Constraint:</strong> Do not use loops; achieve this only with re.sub().</em>


import re

def mask_phone_numbers(text):
    # Mask the first 6 digits and keep the last 4 digits
    pattern = r"\b(\d{6})(\d{4})\b"
    return re.sub(pattern, r"******\2", text)


# Example
text = """
Call me at 9876543210.
Customer care: 9123456789.
Office: 7012345678.
"""

masked_text = mask_phone_numbers(text)
print(masked_text)