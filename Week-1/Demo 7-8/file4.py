# Comma-separated orders. Create orders.txt with these lines: 
# 
# Read the file and turn each line into a dictionary with the keys id, customer, total and status,
#  with total as a number. Collect them in a list, then print 3 delivered orders,
#   Rs 14,400. If your file ends with an empty line, what happens, and how can you skip it?

with open("orders.txt", "w") as file:
    file.write("A101,Noor Foods,4500,delivered\n"
   "A102,Karachi Crafts,12800,pending\n"
   "A103,Noor Foods,2300,delivered\n"
   "A104,Bilal Traders,7600,delivered\n"
   "A105,Karachi Crafts,3900,cancelled")

with open("orders.txt", "r") as file:
   
   orderList = []    
   deliveredTotal = 0
   for line in file:
    line = line.strip()
    if line:
        line = line.split(",")
        orderDict = {"id":line[0], "customer":line[1], "total":int(line[2]), "status":line[3]}
        orderList.append(orderDict)
        
        if orderDict["status"] == "delivered":
           print(orderDict)
           deliveredTotal += orderDict["total"]
    else:
        continue
    
print(f"Total amount: {deliveredTotal:,}")


#if there is a line with an empty string, the program doesn't show any error at all, 
# but if there is a newline character in that empty line, it throws a list index error,
# because when we strip and split it, the list only carries 1 value at index 0, which isn't enough
# for our dictionary setup

# to resolve this, we use an if condition so that if the line is empty, it will skip the iteration
# and move to the next one without crashing, ignoring the current empty line