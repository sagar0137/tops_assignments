#Remove a playlist from the playlist_prices dictionary using the del statement. Print the dictionary after deletion to confirm
#  the change

playlist_price= {
    "Mini": 9,
    "individual": 119,
    "Duo": 149,
    "Family": 179,
    "Student": 59

}
# using of del statement in this dictionary:-
print("Before using del statement")
print(playlist_price)

print("After using del statement ")
del playlist_price["Family"]
del playlist_price["Student"]
print(playlist_price)


# del statement is used to delete the element 