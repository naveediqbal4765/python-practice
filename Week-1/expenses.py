import json

EXPENSES_FILE = "week-1/expenses.json"
APPROVAL_LIMIT = 25000

with open(f"{EXPENSES_FILE}", "w") as file:
    json.dump([
    {"item": "Coffee beans", "category": "Supplies", "amount": 18500},
    {"item": "Milk", "category": "Supplies", "amount": 9200},
    {"item": "Electricity bill", "category": "Utilities", "amount": 27400},
    {"item": "Espresso machine repair", "category": "Equipment", "amount": 35000},
    {"item": "Paper cups", "category": "Supplies", "amount": 6300},
    {"item": "Internet", "category": "Utilities", "amount": 4500},
    {"item": "Social media ads", "category": "Marketing", "amount": 12000},
    {"item": "Barista wages", "category": "Staff", "amount": 60000},
    {"item": "Sugar and syrups", "category": "Supplies", "amount": 7800},
    {"item": "Flyers", "category": "Marketing", "amount": 3500}
  ], file, indent=2)

try:
    with open(f"{EXPENSES_FILE}", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"The {EXPENSES_FILE} file doesn't exist yet!")
    
expensesCount = 0   
total = 0 
categories = {}
LargestEx = 0
needsApproval = []

def totalSpent(amount, total):
    total += amount
    return total
    
def approvalLimit(amount):
    return amount > APPROVAL_LIMIT
    

def LargestExpense(amount,LargestEx):
    if amount > LargestEx:
        LargestEx = amount
    return LargestEx
    
def itemsCategory(amount):
    if category in categories:
        categories[category] += amount
    else:
        categories[category] = amount
    return categories[category]

for expenses in data:
    expensesCount += 1
    amount= expenses["amount"]
    category = expenses["category"]
    
    total = totalSpent(amount,total)
    itemsCategory(amount)
    if amount>LargestEx:
        item = expenses["item"]
    LargestEx = LargestExpense(amount, LargestEx)

    if approvalLimit(amount):
        needsApproval.append((item, amount))
    
    
print(f"Cafe expense report\nExpenses recorded: {expensesCount}\nTotal spent: Rs {total:,}\n\nBy category:")
for name, amnt in categories.items():
    # print(len(name))
    print(f" {name:<11} Rs {amnt:,}")

print(f"\nLargest expense: {item} ({LargestEx:,})") 
print("\nNeeds approval:")
for item, amount in needsApproval:
    # print(len(item))
    print(f" {item:<25} Rs {amount:,}")

with open("week-1/summary.json", "w") as file:
    json.dump({"expense-count": expensesCount, "total": total, "by-category": categories}, file, indent=2)
