#  An API-shaped response. Save this as response.json. 
# It's the shape of data you'll get from real APIs in week 3:
# {
#   "status": "ok",
#   "data": {
#     "customer": {"name": "Noor Foods", "city": "Karachi"},
#     "orders": [
#       {"id": "A101", "total": 4500, "items": ["rice", "oil"]},
#       {"id": "A103", "total": 2300, "items": ["sugar"]},
#       {"id": "A106", "total": 6100, "items": ["flour", "tea", "rice"]}
#     ]
#   }
# }
# Load it and print Noor Foods (Karachi): 3 orders, 6 items, Rs 12,900, 
# working out every value in code. Then save a new file, summary.json, 
# with the keys customer, order_count, item_count and total, and check it in your editor.
import json
with open("response.json", "r") as file:
   response =  json.load(file)

data = response["data"]
customer = data["customer"]["name"]
city = data["customer"]["city"]
items = 0
total = 0
orders = 0

for order in data["orders"]:
  items += len(order["items"])
  total += order["total"]
  orders += 1
print(f"{customer} ({city}): {orders} orders, {items} items, Rs {total:,}")

summary ={
        "customer": customer,
        "order count": orders,
        "item count": items,
        "total": total
}

with open("summary.json", "w") as file:
   json.dump(summary, file, indent=2)