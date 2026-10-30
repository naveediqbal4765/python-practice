# A customer profile. Build one dictionary for a customer that contains a nested dictionary and 
# a list:

# Print the customer's city, their number of orders and the total they've spent. 
# Add a new order of Rs 6,100, then print the new total. Finally, try customer["phone"] 
# and read the error you get. Look up the dictionary .get() method and use it to print 
# No phone number instead of crashing.


customer = {
    "name": "Noor Foods",
    "address": {"city": "Karachi", "area": "Clifton"},
    "order_totals": [4500, 12800, 2300],
}

print(f"Customer's city: {customer["address"]["city"]}, Number of orders: {len(customer["order_totals"])}, Total spent: {sum(customer['order_totals'])}")

customer["order_totals"].append(6100)

print(f"Customer's city: {customer["address"]["city"]}, Number of orders: {len(customer["order_totals"])}, New Total spent: {sum(customer['order_totals'])}")

# customer["phone"]
# this shows a key error, as we didnt define the key phone in our dectionanry

print(customer.get("phone", "no phone number"))

print("new branch")