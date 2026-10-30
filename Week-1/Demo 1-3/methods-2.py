#  Clean an email. Clean " Ali.Khan@GMAIL.com " 
# so it has no spaces and is all lowercase, 
# then print Email: ali.khan@gmail.com (18 characters).

rawGmail = " Ali.khan@GMAIL.com "
strippedGmail= rawGmail.strip()
cleanedGmail= strippedGmail.lower()
print(f"{cleanedGmail}, ({len(cleanedGmail)} characters)")