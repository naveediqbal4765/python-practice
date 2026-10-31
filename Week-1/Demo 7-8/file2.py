# Append, don't erase. Write a function add_note(text) that adds one line to log.txt 
# using append mode. Call it three times, then run your script a second time. 
# How many lines does the file have now? Change the mode to "w" and run it twice more. 
# What changed, and when would you want each behaviour?

def add_note(text):
    with open("log.txt", "w") as file:
        file.write(text)

for line in range(0,3):
    add_note("blah blah blah and more blah\n")

#after running the loop for second time log.txt got 6 lines as we set the range from 0 to index 3
# it prints the same line 3 times in one iteration 

#when i changed the mode to w (write), it erased the appended the lines and wrote the text once
# in w mode it erases the file and writes down the new text on every iteration

# id use a (append) if i want to add more text in file while ill use w (write) when the 
# exsisting text needs to be erased and write new one