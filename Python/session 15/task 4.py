#Build a Flipkart-style order summary: ask the user for item price and quantity, then calculate and print total price. Use try-except-
# else-finally blocks to handle ValueError for invalid input, print the total if successful, and always print 'Thank you for shopping!
# ' in the finally block

try:
    # Take input from the user
    item_price = float(input("Enter the item price (₹): "))
    quantity = int(input("Enter the quantity: "))

except ValueError:
    print("Error: Please enter valid numeric values.")

else:
    # Calculate total price
    total_price = item_price * quantity

    print("\n------ Flipkart Order Summary ------")
    print(f"Item Price : ₹{item_price:.2f}")
    print(f"Quantity   : {quantity}")
    print(f"Total Price: ₹{total_price:.2f}")


finally:
    print("\nThank you for shopping!")