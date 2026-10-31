# Keep stock between runs. Create stock.json containing {"pens": 120, "notebooks": 45, "staplers": 8}. 
# Write a script that loads it, records a sale of 30 notebooks, adds "markers" with 60 in stock if 
# they aren't already there, and saves it back. Run the script three times and open the file after each run. 
# What happens to the notebook count, and what would happen if the count went below zero?
import json

# with open("stock.json", "w") as file:
#     json.dump({"pens": 120, "notebooks": 45, "staplers":8}, file, indent= 2)

with open("stock.json", "r") as file:
    stationary = json.load(file)
    
    stationary["notebooks"] -= 30

    if "markers" not in stationary:
        stationary["markers"] = 60   

with open("stock.json", "w") as file:
    json.dump(stationary, file, indent=2)
    
# the notebook count decreases by 30 every time we run the file
# python will continue to subtract from the stock even if the value drops below zero into negative numbers.