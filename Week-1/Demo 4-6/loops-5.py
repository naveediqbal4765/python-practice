#  Reorder report. For each product below its reorder_level, 
# order enough to bring its stock up to twice the reorder level:
# Copy
# inventory = [
#     {"name": "Notebook", "stock": 8, "reorder_level": 15, "unit_cost": 90},
#     {"name": "Pen", "stock": 140, "reorder_level": 50, "unit_cost": 25},
#     {"name": "Stapler", "stock": 2, "reorder_level": 5, "unit_cost": 650},
#     {"name": "Marker", "stock": 30, "reorder_level": 30, "unit_cost": 120},
#     {"name": "Folder", "stock": 11, "reorder_level": 20, "unit_cost": 60},
# ]
# Print one line per product to reorder, 
# such as Reorder 22 x Notebook (Rs 1,980), and finish with the total cost (expected: Rs 8,920). 
# If no product needs reordering, print All stock OK instead. Test that by raising every stock level.
# Why isn't Marker on the list?

inventory = [
    {"name": "Notebook", "stock": 8, "reorder_level": 15, "unit_cost": 90},
    {"name": "Pen", "stock": 140, "reorder_level": 50, "unit_cost": 25},
    {"name": "Stapler", "stock": 2, "reorder_level": 5, "unit_cost": 650},
    {"name": "Marker", "stock": 30, "reorder_level": 30, "unit_cost": 120},
    {"name": "Folder", "stock": 11, "reorder_level": 20, "unit_cost": 60},
]

total = 0
totalCost = 0
reordered = 0
for x in inventory:
    if x["stock"] < x["reorder_level"]:
        reorder = (x["reorder_level"] * 2) - x["stock"]
        total = reorder * x["unit_cost"]
        totalCost += total
        reordered += 1 
        print (f"Reorder {reorder} x {x["name"]} (Rs {total:,})")

if reordered == 0:
        print("All stock Okay")
else:
    print(f"Total = {totalCost:,}")

# arker isnt on the list because we only reorder products whose stock is belowthe reorder level. 
# markers stock is equal to its reorder level so it is not below it.