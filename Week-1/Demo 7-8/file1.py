# A shopping list. Write four items to shopping.txt, one per line. 
# Then read the file back and print each item numbered: 1. Rice, 2. Oil and so on.

with open("shopping.txt","w") as file:
    file.write(" rice\n oil\n tea\n pickle\n")

with open("shopping.txt", "r") as file:

    x=0
    for line in file:
        x += 1
        print(f"{x}. {line.strip()}")

