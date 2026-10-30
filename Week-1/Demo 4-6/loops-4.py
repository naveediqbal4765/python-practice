# Totals per customer. Starting from this list, 
# build a dictionary that holds each customer's total spend:

# You need to check whether a customer is already in the dictionary: 
# look up how in works with dictionaries. 
# Then look up the dictionary .items() method and loop over your result to print:

# Noor Foods: Rs 12,900
# Karachi Crafts: Rs 16,700
# Bilal Traders: Rs 7,600
# -------------------------------------------

# first we will build an empty dictionary called newDictionary

# run a for loop and initialize a variable called order

# in the first iteration we'll store the new customers name and their total in two separate
# variables

# use an if condition to check if that customer is already in our newDictionary

# at the first iteration as we have an empty dictionary the if condition will return false

# well use the else condition to store the customers name and the total we just got in the first iteration
# in newDictionary

# at the second iteration, the if else conditions will check the facts as i explained above and store the
# values

# when the if condition gets an existing customer it will add up the existing total with the new total.
# the else condition will work as mentioned before

# at the end we'll get our newDictionary with non repeating customers and totals

# Then we'll run a new for loop with variables for the keys and values in newDictionary
# that we just loaded. We'll use the .items() method to print both key and value
# -------------------------------

orders = [
    {"customer": "Noor Foods", "total": 4500},
    {"customer": "Karachi Crafts", "total": 12800},
    {"customer": "Noor Foods", "total": 2300},
    {"customer": "Bilal Traders", "total": 7600},
    {"customer": "Karachi Crafts", "total": 3900},
    {"customer": "Noor Foods", "total": 6100},
]

newDictionary = {}

for order in orders:
    newCustomer = order["customer"]
    newCustomersTotal = order["total"]

    if newCustomer in newDictionary:
        newDictionary[newCustomer] += newCustomersTotal

    else:
        newDictionary[newCustomer] = newCustomersTotal

for newCustomer, newCustomersTotal in newDictionary.items():
    print(f"{newCustomer}: Rs {newCustomersTotal:,}")