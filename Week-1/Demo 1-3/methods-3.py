# A receipt line. The item name is " wireless MOUSE ", the price is 2499 and the quantity is 3. 
# Print exactly: Wireless Mouse x3 = Rs 7,497. 
# Work out the total in code; don't type the number.

itemName = "wireless MOUSE"
price = 2499
quantity = 3

print(f"{itemName.title()} x{quantity} = Rs {price*quantity}.")