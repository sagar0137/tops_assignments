#Write a Python function using re.search() that checks if a given string contains a valid date in the format DD/MM/YYYY (e.g., 
# 25/06/2024), and returns True if found, otherwise False.<br><br><em><strong>Hint:</strong> Use the pattern '\b\d{2}/\d{2}/\d{4}\b'
# .</em

import re

def contains_valid_date(text):
    # Pattern for DD/MM/YYYY
    pattern = r"\b\d{2}/\d{2}/\d{4}\b"

    # Search for the pattern
    if re.search(pattern, text):
        return True
    else:
        return False


# Example usage
print(contains_valid_date("Today's date is 25/06/2024."))   # True
print(contains_valid_date("Meeting on 5/6/2024."))           # False
print(contains_valid_date("No date here."))                  # False
print(contains_valid_date("Birthday: 01/01/2000"))           # True