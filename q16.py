from collections import OrderedDict
from operator import itemgetter
from itertools import groupby

# 1. Create first dictionary (insertion order preserved by default in Python 3.7+)
stocks1 = {
    'AAPL': 750,
    'GOOG': 1200,
    'MSFT': 800,
    'AMZN': 1500,
    'TSLA': 800,
    'NFLX': 500
}

print("Stocks1:", stocks1)

# 2. Find minimum and maximum price
min_stock = min(stocks1.items(), key=itemgetter(1))
max_stock = max(stocks1.items(), key=itemgetter(1))

print("Minimum price:", min_stock)
print("Maximum price:", max_stock)

# 3. Sort items according to price
sorted_stocks1 = dict(sorted(stocks1.items(), key=itemgetter(1)))
print("Sorted stocks1:", sorted_stocks1)

# 4. Create second dictionary
stocks2 = {
    'AAPL': 750,
    'GOOG': 1250,
    'MSFT': 800,
    'FB': 600,
    'TSLA': 900
}

print("Stocks2:", stocks2)

# 5. Items only in first dictionary
only_in_first = stocks1.keys() - stocks2.keys()
print("Only in first:", only_in_first)

# 6. Items whose prices do not match
price_mismatch = {k for k in stocks1.keys() & stocks2.keys() if stocks1[k] != stocks2[k]}
print("Price mismatch:", price_mismatch)

# 7. Remove duplicate items from first dictionary (duplicate values)
unique_stocks1 = {}
seen_prices = set()

for k, v in stocks1.items():
    if v not in seen_prices:
        unique_stocks1[k] = v
        seen_prices.add(v)

print("Stocks1 without duplicate prices:", unique_stocks1)

# 8. Sort both dictionaries by increasing prices
sorted_stocks1 = dict(sorted(stocks1.items(), key=lambda x: x[1]))
sorted_stocks2 = dict(sorted(stocks2.items(), key=lambda x: x[1]))

print("Sorted stocks1:", sorted_stocks1)
print("Sorted stocks2:", sorted_stocks2)

# 9. Group items in first dictionary by price in multiples of 500
# Define grouping key
def group_key(item):
    return (item[1] // 500) * 500

# Sort first for groupby
sorted_items = sorted(stocks1.items(), key=lambda x: (x[1] // 500) * 500)

grouped = {}
for key, group in groupby(sorted_items, key=group_key):
    grouped[key] = list(group)

print("Grouped stocks1 (by multiples of 500):")
for k, v in grouped.items():
    print(f"{k}-{k+499}:", v)

# 10. Find items with price = 800 from both dictionaries
price_800_stocks1 = [k for k, v in stocks1.items() if v == 800]
price_800_stocks2 = [k for k, v in stocks2.items() if v == 800]

print("Stocks in stocks1 with price 800:", price_800_stocks1)
print("Stocks in stocks2 with price 800:", price_800_stocks2)