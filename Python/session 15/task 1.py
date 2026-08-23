#Write a Python function safe_divide(a, b) that returns the result of a divided by b, and handles ZeroDivisionError by returning
#  the string 'Cannot divide by zero'.

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


# Example usage
print(safe_divide(10, 2))   # Output: 5.0
print(safe_divide(10, 0))   # Output: Cannot divide by zero
