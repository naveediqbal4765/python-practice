# Return or print? Write add_tax(subtotal, rate=0.18). 
# The rate=0.18 part is a default value: it's used when you don't pass a rate. 
# Check that add_tax(7200) returns 8496.0 and add_tax(7200, 0.05) returns 7560.0. 
# Now write a second version that uses print() instead of return, 
# store its result in a variable and print the variable. What do you get, and why?

def add_tax(subtotal, rate=0.18):
    tax = subtotal * rate
    return subtotal + tax

print(add_tax(7200, 0.05))
print(add_tax(7200))

def addTax(subtotal, rate=0.18):
    tax = subtotal * rate
    newSubTotal = subtotal + tax
    print(f"new fuc: {newSubTotal}")

result = addTax(7200, 0.05)
print(result)

# i got 7560.0 and None.
# The 7560.0 comes from the print inside addTax which only displays the value on screen
# as addTax has no return statement so it gives back None by default.
