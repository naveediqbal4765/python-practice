# 1. Python to JSON. Create a dictionary for a product with the keys name, 
# price, in_stock (a boolean) and discount (set to None). Print it with print(), 
# then print json.dumps() of it, then json.dumps() with indent=2. 
# Write a comment listing every difference you can see between the Python and the JSON

import json
product = {"price":200 , "in_stock": False, "discount": None}

print("Without indent: ",json.dumps(product))
print("With indent: ",json.dumps(product, indent=2))