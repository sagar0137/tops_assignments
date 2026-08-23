#Write a function update_playlist_price(playlist, new_price) that updates the price of a given playlist in the playlist_prices
# dictionary. Test it by updating the price of any one playlist and printing the updated dictionary


playlist_price= {
    "Mini": 9,
    "individual": 119,
    "Duo": 149,
    "Family": 179,
    "Student": 59

}

def update_playlist_price(playlist,new_price):
    if playlist in playlist_price:
        playlist_price[playlist] = new_price
        print(f"Price of ",{playlist}, "update successfull.")
    else:
        print(f"Playlist ",{playlist}, "not found.")



update_playlist_price("unknown",344)
print(playlist_price)



update_playlist_price("individual",249)
update_playlist_price("Student",599)

print('Updated playlist is:-')
print(playlist_price)
for price in  playlist_price.items():
    print(price)

