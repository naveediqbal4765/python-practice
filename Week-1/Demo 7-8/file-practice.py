with open("notes.txt","w") as file:
    file.write("this is my file program part 2\n")
    file.write("this is my file program part 3\n")

with open("notes.txt", "a") as file:
    file.write("this is my file program part 4")

with open("notes.txt", "r") as file:
    text = file.read()

print (text)