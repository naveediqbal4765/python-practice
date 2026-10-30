# Stock levels. Create a dictionary of stock counts: 
# {"pens": 120, "notebooks": 45, "staplers": 8}. 
# The shop sells 30 notebooks: update the count by subtracting from the current value,
# not by typing 15. Add a new product, "markers", with 60 in stock. 
# Print how many products there are (use len()) and then the whole dictionary.

stock = {
    "pens" : 120,
    "notebooks" : 45,
    "staplers" : 8
}


soldNotebooks = 30
stock["notebooks"] = stock["notebooks"] - soldNotebooks

stock["markers"] = 60

print(f"Notebooks left: {stock["notebooks"]}, Dictionary: {stock}, Number of Products: {len(stock)}")