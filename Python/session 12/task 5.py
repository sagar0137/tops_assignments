#Use ChatGPT or Copilot to generate a Python code snippet that uses map(), filter(), and reduce() together to process a list of
#  numbers: first double each number, then filter to keep only numbers greater than 100, and finally sum the result. Paste and 
# test the generated code with the list [40, 60, 80, 120].
from functools import reduce

numbers=[40,60,80,120]
print("Original number is:-",numbers)

print("using map method :-" )
map_number=list(map(lambda x:x*2,numbers))
print("doubled number:-",map_number)

print("using of flter greater than 100:-")
filtered=list(filter(lambda x:x>100,numbers))
print("number greater than 100 are:-",filtered)

print("using reduce method:-")
reduced= reduce(lambda x,y:x+y,numbers)
print('total of the numbers is :-',reduced) 