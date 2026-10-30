# Totals by status. Write total_by_status(orders, status) that takes a list of order dictionaries
# and a status, and returns the sum of the totals with that status. 
# Using the orders list from Demo 5, check that "delivered" gives 6800, 
# "pending" gives 12800 and "cancelled" gives 0.

orders = [
    {"id": "A101", "total": 4500, "status": "delivered"},
    {"id": "A102", "total": 12800, "status": "pending"},
    {"id": "A103", "total": 2300, "status": "delivered"},
]

def total_by_status(orders, status):
    total = 0
    for order in orders:
        if order["status"] == status:
            total += order["total"]
    return total

print(total_by_status(orders,"cancelled"))

