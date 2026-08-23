#.Create an abstract class PaymentMethod with an abstract method pay(amount). Then, create two subclasses: UPI and CreditCard,
#  each implementing the pay method with a print statement showing how the payment would be processed.<br><br><em><strong>Hint:
# </strong> Use the abc module for abstraction.</em>

from abc import ABC, abstractmethod

# Abstract class
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Subclass 1
class UPI(PaymentMethod):

    def pay(self, amount):
        print(f"Processing UPI payment of ₹{amount}...")


# Subclass 2
class CreditCard(PaymentMethod):

    def pay(self, amount):
        print(f"Processing Credit Card payment of ₹{amount}...")


# Create objects
upi_payment = UPI()
card_payment = CreditCard()

# Make payments
upi_payment.pay(500)
card_payment.pay(1200)
