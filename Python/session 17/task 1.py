#Use the math module to calculate the square root, factorial, and value of pi for given numbers, and print each result

import math

# Given numbers
number_for_sqrt = 64
number_for_factorial = 6

# Calculate square root
sqrt_result = math.sqrt(number_for_sqrt)

# Calculate factorial
factorial_result = math.factorial(number_for_factorial)

# Get the value of pi
pi_value = math.pi

# Print the results
print("Square Root:")
print(f"√{number_for_sqrt} = {sqrt_result}")

print("\nFactorial:")
print(f"{number_for_factorial}! = {factorial_result}")

print("\nValue of Pi:")
print(f"π = {pi_value}")