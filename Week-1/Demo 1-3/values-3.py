# Splitting a bill. Four friends split a Rs 4,750 dinner. 
# Print each person's share using /. 
# Then look up the // and % operators and use them to print how 
# many whole rupees each person pays and how many rupees are left over.

totalBill = 4750
numberOfFriends = 4
eachPersonShare = totalBill/numberOfFriends
mod = totalBill%numberOfFriends
whole = totalBill//numberOfFriends

print(f" Each Person's share: {eachPersonShare}, Left over: {mod}, Rupees in whole: {whole}")