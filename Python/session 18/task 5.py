#Use ChatGPT to generate a regex pattern that matches Flipkart-style order IDs (e.g., OD123456789012345000) and test it in Python 
# using re.search() on sample order strings.

import re

# Regex pattern:
# OD followed by exactly 18 digits
pattern = r"\bOD\d{18}\b"

# Sample order strings
orders = [
    "Your Flipkart order ID is OD123456789012345000.",
    "Order shipped: OD987654321098765432",
    "Invalid order: OD12345",
    "Wrong format: AB123456789012345000",
    "Another valid ID: OD111122223333444455"
]

# Test each string
for order in orders:
    if re.search(pattern, order):
        print(f"Match Found: {re.search(pattern, order).group()}")
    else:
        print("No valid order ID found.")