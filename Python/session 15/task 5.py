#Use ChatGPT or Copilot to generate a Python code snippet that asks for two numbers and divides them, handling both ZeroDivisionError
#  and ValueError. Paste the generated code, run it, and write one line about what you learned from the AI's approach.


try:
    # Ask the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Divide the numbers
    result = num1 / num2

except ValueError:
    print("Error: Please enter valid numeric values.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print(f"Result: {result}")

finally:
    print("Program execution completed.")
    