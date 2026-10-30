# Order codes. Look up the .replace() and .upper() methods. 
# Turn the raw code " ord-2024-0042 " into ORD20240042, 
# then print Order ORD20240042 has 11 characters. 
# Can you do the whole clean-up in one line by chaining methods?

rawCode = "ord-2024-0042"
cleanedCode = rawCode.replace("-","")
print(cleanedCode.upper())