#Write a Python script that demonstrates the lifetime of a local variable inside a function versus a global variable by printing 
# their values before, during, and after a function call. Use variable names similar to 'user_status' and 'app_status',
#  inspired by WhatsApp online/offline status.
# Global variable
app_status = "WhatsApp is Running"


def check_user_status():
    # Local variable
    user_status = "Online"

    print("Inside Function:")
    print("App Status  :", app_status)      # Accessing global variable
    print("User Status :", user_status)     # Accessing local variable


# Before function call
print("Before Function Call:")
print("App Status :", app_status)

# Calling the function
print("\nCalling Function...\n")
check_user_status()

# After function call
print("\nAfter Function Call:")
print("App Status :", app_status)

# Trying to access the local variable outside the function
try:
    print("User Status :", user_status)
except NameError:
    print("User Status : Cannot access (local variable no longer exists)")
    