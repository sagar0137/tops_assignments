#Use filter() and a lambda function to extract only those Flipkart product names from a list that start with the letter 'S' 
# (case-insensitive).

flipkart_products = [
    'Apple iPhone 15', 'Apple AirPods Pro', 'Samsung Galaxy S24', 'Samsung Smart TV',
     'Sony Headphones', 'Boat Rockerz 450', 'Boat Airdopes 141', 'Dell Inspiron Laptop',
     'Dell Wireless Mouse', 'HP Pavilion Laptop']
print(flipkart_products)

result=list(filter(lambda product:product.startswith("S"),flipkart_products))
print(result)