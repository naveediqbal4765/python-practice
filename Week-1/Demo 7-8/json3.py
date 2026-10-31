# Save in one script, load in another. 
# In save_orders.py, save the orders list from the demo to orders.json. 
# Open the file in your editor and look at it. 
# Then, in a separate file, load_orders.py, load it and print 3 orders, Rs 19,600 in total.

import json
total = 0
with open("orders.json", "r") as file:
    orders = json.load(file)
    for line in orders:
        print(line)
        total += line["total"]

print (f"Total: Rs {total:,}")