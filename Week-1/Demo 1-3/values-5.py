# Packing boxes. A shop is shipping 23 items, and each box holds 6. 
# Using only arithmetic (no if), print the number of full boxes, the 
# number of items left over, and the total number of boxes needed, 
# including a partly full one (expected: 3, 5 and 4). 
# Each box costs Rs 120 to ship: print the shipping cost. 
# Test your code with 24 items. Does the box count still come out right?

import math

boxCost = 120
totalItems = 23
eachBoxHolds = 6
numberOfBoxes = math.ceil(totalItems/eachBoxHolds)
numberOfFullBoxes = totalItems//eachBoxHolds
print(f"Number of full boxes: {numberOfFullBoxes}, Items packed: {numberOfFullBoxes*eachBoxHolds} ")
print(f"Number of leftover items: {totalItems-(numberOfFullBoxes*eachBoxHolds)}")
print(f"Total number of boxes including partly full one: {numberOfBoxes}")
print(f"Total cost : {(numberOfBoxes*boxCost)}")
