#  Discount and tax. A phone costs Rs 15,000. Apply a 10% discount, 
# then add 18% tax to the discounted price, and print the final price. 
# Now do it the other way round: tax first, then the discount. 
# Do you get the same answer? Write a comment in your code explaining why or why not.

phoneCost = 15000
discount = 10

discountedPrice =15000 - (15000 * (discount/100)) 
print(f"Price after 10% discount is {discountedPrice}")

tax = 18
totalPrice = discountedPrice + (discountedPrice * (tax/100))

print(f"Total price after 10% discount and adding 18% tax is {totalPrice}")