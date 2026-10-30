# Create a list of three prices: [850, 1200, 400]. 
# Print the last price and the sum of all three. 

prices = [850, 1200, 400]

print(f"last price: {prices[2]}, Sum of all three prices: {sum(prices)}")



# Then create a dictionary for one product with the keys name, price and in_stock. 
# Change in_stock to False and print just the product's name.

Products ={
    "name" : "Blahblah",
    "price" : 850,
    "in_stock" : True
}

Products["in_stock"] = "False"
print(Products["name"])