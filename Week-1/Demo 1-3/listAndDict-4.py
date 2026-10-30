# A list of orders. Create a list of three order dictionaries, each with id, 
# customer and total. Without a loop:
# Print the customer of the second order.
# The third order gets a Rs 500 discount: change its total.
# Add a fourth order to the end of the list.
# Print 4 orders. The first is A101 and the last is A104., taking every value from the list.

orders = [ 
    {"id" : 1, "customer" : "customer1", "total" : 1000}, 

    { "id" : 2, "customer" : "customer2", "total" : 120 },

    { "id" : 3, "customer" : "customer3", "total" : 4000 }
    ]

print(f"Seconed order customer: {orders[1]["customer"]}")
discount = 500

orders[2]["total"] = orders[2]["total"]-discount

print(f"Total after Rs 500 discount: {orders[2]["total"]}")

orders.append({"id" : 4, "customer" : "customer4", "total" : 500})

print(orders)