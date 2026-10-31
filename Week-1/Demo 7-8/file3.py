# A week of sales. Create sales.txt in your editor with one number per line: 
# 18500, 22300, 19800, 25400, 31200, 42800 and 38600. 
# Read the file, convert each line to a number, 
# and print the weekly total and daily average using
# your format_rupees() function (expected: Rs 198,600 and Rs 28,371). 
# What error do you get if you forget to convert?

with open("sales.txt", "w") as file:
    file.write("18500\n 22300\n 19800\n 25400\n 31200\n 42800\n 38600")

with open("sales.txt", "r") as file:
    
    total = 0
    length = 0
    for line in file:
        lines = int(line)
        total += lines
        length +=1
        
avg = total//length
print(f" Total: Rs {total:,}\n Average: Rs {avg:,}") 

#it shows type error, if not converted to int