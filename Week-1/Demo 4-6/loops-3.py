# The biggest order. Using the orders list from the demo, 
# find the order with the highest total without using max(). 
# Keep a "biggest so far" variable and update it inside the loop. 
# Print Biggest order: A102 (Rs 12,800). What happens if two orders have the same highest total?

# -------------------------------------------------------
# We will declare two variables biggestSoFar as an empty string and highestTotal
# as an int with a value of zero.

# then run a for loop, and declare a variable x to represent each fact from the dictionary orders

# use an if condition to check if the key (total) with reference to x is greater than highestTotal

# in the first iteration it will store the 0th index's total value in highestTotal because we
# already gave it the value 0 during initialization.

# in the second iteration as the 0th index's total value is smaller than the second one, 
# it will swap the value.

# the loop will iterate until all the facts are accessed then well get the highest number
# in highestTotal.

# as we also declared a string type variable (biggestSoFar), we'll use that to store the id of
# the highest value we got.

# outside the loop we will print the id and the highest total value as output.
# --------------------------------------------------

orders = [
    {"id": "A101", "total": 4500, "status": "delivered"},
    {"id": "A102", "total": 12800, "status": "pending"},
    {"id": "A103", "total": 2300, "status": "delivered"},
]

biggestSOfar = ""
highestTotal = 0

for x in orders:
    if x["total"] > highestTotal:
        highestTotal = x["total"]
        biggestSOfar = x["id"]

print(f"Biggest order: {biggestSOfar} (Rs {highestTotal:,})")


# if two orders have the same highest total the loop will print the first one it finds
# during the iteration.