#Create a new virtual environment using venv, activate it, and install the statistics and requests packages via pip. Then, 
# write a script that uses statistics.mean() to calculate the average of a list of numbers.

import statistics

# List of numbers
numbers = [12, 18, 25, 30, 45]

# Calculate the average
average = statistics.mean(numbers)

# Print the result
print("Numbers:", numbers)
print("Average:", average)
