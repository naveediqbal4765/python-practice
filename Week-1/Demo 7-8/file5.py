# Write a report. Using your list from problem 4, work out each customer's total, 
# leaving out cancelled orders. Write the result to report.txt so the file contains exactly:

# Copy
# Order report
# Noor Foods: Rs 6,800
# Karachi Crafts: Rs 12,800
# Bilal Traders: Rs 7,600
# Total: Rs 27,200
# Add a sixth order to orders.txt and run your script again. The report should change with 
# no other code changes.

import file4

newDict = {}
subtotal = 0
for line in file4.orderList:
    if line["status"] != "cancelled":
        customer = line["customer"]
        total = line["total"]
        
        if customer in newDict:
         newDict[customer] += total
        else:
           newDict[customer] = total

        subtotal += total

with open("report.txt", "w") as file:
   file.write("Order Report\n")
   for customer, total in newDict.items():
      file.write(f"{customer}: Rs {total:,}\n")
      
   file.write(f"Total: Rs {subtotal:,}\n")