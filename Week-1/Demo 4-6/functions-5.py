# Refactor the reorder report. Take your reorder report from Demo 5, problem 5, 
# and split it into three small functions:

# needs_reorder(product) returns True or False
# reorder_quantity(product) returns how many to order
# reorder_cost(product) returns the cost of that order, using reorder_quantity()
# Rewrite the loop so it uses these functions, and check you still get the same lines and
# the same total (Rs 8,920). Write a comment explaining one way the new version is easier to read, 
# test or change than the old one.

inventory = [
    {"name": "Notebook", "stock": 8, "reorder_level": 15, "unit_cost": 90},
    {"name": "Pen", "stock": 140, "reorder_level": 50, "unit_cost": 25},
    {"name": "Stapler", "stock": 2, "reorder_level": 5, "unit_cost": 650},
    {"name": "Marker", "stock": 30, "reorder_level": 30, "unit_cost": 120},
    {"name": "Folder", "stock": 11, "reorder_level": 20, "unit_cost": 60},
]

def needs_reorder(x):
       return x["stock"] < x["reorder_level"]

def reorder_quantity(x):
     return x["reorder_level"] * 2 - x["stock"]

def reorder_cost(x):
     return reorder_quantity(x) * x["unit_cost"]

totalCost = 0
for x in inventory:
     if needs_reorder(x):
        reorder = reorder_quantity(x)
        total = reorder_cost(x)
        totalCost += total
        print (f"Reorder {reorder} x {x["name"]} (Rs {total:,})")

print(f"Total: Rs {totalCost:,}")