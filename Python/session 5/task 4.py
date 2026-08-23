#Create a tuple called insta_filters with 4 Instagram filter names. Try to update the second filter and observe what error you get. 
# #Explain in a comment why this happens.<br><br><em><strong>Hint:</strong> Tuples are immutable, so direct assignment won't work.
# </em>

'''
insta_filters= ("Clarendon", "Juno", "Lark", "Gingham")
insta_filters["Juno"] = "love filter "
print(insta_filters)
'''
# here we tried to update element of tuple but it give type error (TypeError: 'tuple' object does not support item assignment):-
# it happens because tuple is immutable 
print("Here we tried to update element of tuple but it give type error ")
