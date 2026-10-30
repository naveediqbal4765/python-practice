# Sales tax. An order's subtotal is Rs 7,200 and sales tax is 18%. 
# Print the tax amount and the total with tax (expected: 1296.0 and 8496.0). 
# Print the type of the tax amount. Why is it a float when the subtotal was an int?

subtotal = 7200
tax = 18

taxAmount = 7200 * (18/100)

totalWithTax= taxAmount+subtotal

print(totalWithTax)
print(type(totalWithTax))

#because we got the taxAmount in float, 
# which turned the total amount into float at the end both datatypes are numbers and 
# python converts it without declaring the variable.