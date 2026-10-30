# Store a shop's daily sales for one week in a list:'
# ' [18500, 22300, 19800, 25400, 31200, 42800, 38600]. Print Monday's and Sunday's sales, '
# 'the weekly total and the daily average, formatted as Rs with commas and no decimals. '
# 'Then look up max() and min() and print the best and worst days' sales

sales = [18500, 22300, 19800, 25400, 31200, 42800, 38600]
print(f"Monday sales: Rs {sales[1]}, Sunday sales: Rs {sales[6]}")
weeklyTotal = sum(sales)
dailyAvg = weeklyTotal/len(sales)
bestDay = max(sales)
worstDay = min(sales)

print(f"Weekly toal: Rs {weeklyTotal}, Daily average: Rs {dailyAvg}, Best day sales: Rs {bestDay}, Worst day sales: Rs {worstDay}")