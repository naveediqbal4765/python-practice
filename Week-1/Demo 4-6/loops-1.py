#  Delivered revenue. Using the same orders list from the demo, 
# write a loop that adds up the totals of the delivered orders only, 
# then prints Delivered revenue: Rs 6,800.

orders = [
    {"id": "A101", "total": 4500, "status": "delivered"},
    {"id": "A102", "total": 12800, "status": "pending"},
    {"id": "A103", "total": 2300, "status": "delivered"},
]

deliveredRevenue = 0

for order in orders:
    if order["status"] == "delivered":
        deliveredRevenue += order["total"]

print(f"Delivered revenue: Rs {deliveredRevenue}")
