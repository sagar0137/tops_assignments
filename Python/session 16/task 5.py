#Build a generator function called cashback_generator(transactions) that takes a list of Paytm transaction amounts and yields 5% 
# cashback for each transaction. Print out the cashback values for all transactions.

# Generator function
def cashback_generator(transactions):
    for amount in transactions:
        yield amount * 0.05   # 5% cashback

# List of Paytm transaction amounts
transactions = [500, 1200, 750, 300, 1500]

# Print cashback for each transaction
print("Paytm Cashback Details")
print("-" * 30)

for cashback in cashback_generator(transactions):
    print(f"Cashback: ₹{cashback:.2f}")
