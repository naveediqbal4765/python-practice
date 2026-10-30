#json: javascript object notation

import json

import json

order = {"id": "A102", "customer": "Noor Foods", "total": 12800, "paid": False, "notes": None}

text = json.dumps(order)
print(text)

same_order = json.loads(text)
print(same_order["customer"])

with open("notes.txt", "w") as file:
    file.write(text)

with open("notes.txt", "r") as file:
    text = file.read()
