# Numbered items. Loop over the prices [850, 1200, 400, 3100, 650] and
# print each one numbered, as Item 1: Rs 850, Item 2: Rs 1,200 and so on, 
# using a counter variable. At the end, print the total and how many items cost more than Rs 1,000.

prices = [850, 1200, 400, 3100, 650]
i = 0
items = 0
total = 0
for x in prices:
    i += 1
    print(f"{i}:{x}")
    total += x 

    if x > 1000:
        items += 1

print(f"{items} items cost more than Rs 1,000")
print(f"Total: {total}")