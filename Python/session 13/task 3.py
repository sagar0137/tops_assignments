#Given the following code, identify whether the variable 'count' is local or global in each function, and explain what will be printed 
# when run:
count = 10   # this count variable is global because it is declared outside any function, it can be accessed for anywhere in program

def update_count():
    count = 5    # this count is local variable because it is declared inside update_count function
    print("Inside:", count)

update_count()
print("Outside:", count)

# when we run this program firstly it will print inside 5 because it is inside of function because we called update function firstly 
# then we write code to print outside of function so this will print the gloabal variable 
# if we did not give local varibale , the global variable will print for both 
