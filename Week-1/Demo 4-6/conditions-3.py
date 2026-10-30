# Stock check. Given stock = 12 and quantity, print:

# Invalid quantity if the quantity is 0 or less
# Only 12 left in stock if the quantity is more than the stock
# Confirmed. 7 left after this order otherwise (here, for a quantity of 5)

stock = 12
quantity = 0

if quantity > 0:
    if quantity >= 12:
        print (f"Only {stock} left in stock.")
    
    else:
        stock -= quantity
        print(f"Confirmed. {stock} left after this order")

else:
    print("Invalid quantity")

