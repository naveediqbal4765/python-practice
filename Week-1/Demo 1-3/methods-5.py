# Usernames. You have first = " bilal ", last = "QURESHI " and city = "lahore". 
# Look up string slicing (for example text[0:3]). 
# Build the username bilal.qureshi_lah 
# (lowercase first name, a dot, lowercase last name, an underscore and 
#  the first three letters of the city), then print:
# Welcome, Bilal Qureshi from Lahore!
# Your username is bilal.qureshi_lah (17 characters).

first = "bilal"
last = "QURESHI"
city = "lahore"

print(f"Welcome, {first.title()} {last.title()} from {city.title()}!")
print(f"Your username is {first.lower()}.{last.lower()}_{city[0:3]}")
