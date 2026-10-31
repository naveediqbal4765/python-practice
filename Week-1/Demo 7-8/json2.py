# JSON to Python. An API sends you this text:

# Copy
#
# Turn it into a dictionary with json.loads(). Print the name, the number of tags and 
# the type of active. Then try text["name"] before converting it. Why doesn't that work?
import json

text = '{"name": "Amna Raza", "plan": "pro", "active": true, "tags": ["vip", "lahore"]}'
# print(text["name"])
text = json.loads(text)

print(f"{text["name"]}\n{len(text["tags"])}\n{type(text["active"])}")

# it shows TypeError: string indices must be integers, not 'str'
# because it treats the text like a string