#Write a lambda function that takes a price in rupees and returns the price after adding 18% GST. Test it on the prices 100, 250, 
# and 500
prices=[100,250,500]
print("prices before add gst:-",prices)
#gst=list(map(lambda x:x*0.18,prices))
gst_price = list(map(lambda x:x+x*0.18,prices))
print("prices after add GST:-",gst_price)
