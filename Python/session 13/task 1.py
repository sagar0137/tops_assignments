#Write a recursive function in Python called reverse_string(s) that takes a string and returns it reversed (e.g., 'hello' becomes 
# 'olleh')

def reverse_string(s):
    # Base case
    if len(s) <= 1:
        return s

    # Recursive case
    return reverse_string(s[1:]) + s[0]


# Example
text = "hello"
print("Original String:", text)
print("Reversed String:", reverse_string(text))
