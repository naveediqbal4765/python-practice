#  Formatting rupees. Write a function format_rupees(amount) that returns text such as Rs 12,800.
# Test it with 12800, 999 and 1250000. Then use it to print Noor Foods owes Rs 11,520.

def format_rupees(amount):
    return print(f"Rs {amount:,}")

format_rupees(1250000)
