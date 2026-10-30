# Ticket triage. A support ticket has a plan ("free", "pro" or "enterprise"), 
# hours_open and a message. Look up how in works with strings (for example "refund" in text). 
# Print its priority:

# Urgent if the plan is enterprise and it has been open more than 4 hours
# High if the message mentions "refund" or "charged twice" in any capitalisation, 
# or the plan is pro and it has been open more than 24 hours 
# Normal otherwise
# Check your code against these cases:

# plan	hours_open	message	Expected
# "enterprise"	6	"Login is broken"	Urgent
# "free"	1	"I want a REFUND"	High
# "pro"	30	"Dashboard is slow"	High
# "enterprise"	2	"Question about invoices"	Normal
# An enterprise ticket that has been open 6 hours and asks for a refund should be Urgent. 
# # Does your code agree? Write a comment explaining why the order of your checks matters.


plan = "enterprise"
hoursOpen = 2
message = "question about invoices"
Expected = ""

if plan == "enterprise" and hoursOpen > 4:
    expected = "Urgent"

elif (message == "REFUND" or message == "CHARGED TWICE") or (plan == "pro" and hoursOpen == 24):
    expected = "High"

else:
    expected = "Normal"

print (expected)

    