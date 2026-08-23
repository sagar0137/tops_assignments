#Create a function get_delivery_charge(amount, city='Ahmedabad') that returns a delivery charge: Rs. 30 for Ahmedabad,
#  Rs. 50 for other cities. Call it with and without the city argument to see both results

def get_delivery_charge(amount, city='Ahemdabad'):
    if city == 'Ahemdabad':
        return "delivery_charge rs 30 for Ahemdabad"
    else:
        return "Rs 50 for other cities"
print("delivery charge for other cities:-")
charge=get_delivery_charge(1000,"prayagraj")
print(charge)
print("delivery charge for ahemdabad only:-")
ahemda=get_delivery_charge(1200)
print(ahemda)
