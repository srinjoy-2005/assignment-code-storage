import random
random.seed(42)

num_stocks = 10
stocks_1 = {}
for i in range(num_stocks):
    stocks_1[f"stock{i}"] = 100 * random.randint(1,50)
    print(f"stock{i}: {stocks_1[f"stock{i}"]}")

stock_with_min_value = min(stocks_1,key=stocks_1.get)
stock_with_max_value = max(stocks_1,key=stocks_1.get)

print(f"stock_with_max_value: {stock_with_max_value} - {stocks_1[stock_with_max_value]}")
print(f"stock_with_min_value: {stock_with_min_value} - {stocks_1[stock_with_min_value]}")

stocks_1_sorted:dict = dict(sorted(stocks_1.items(),key= lambda item:item[1]))
for key,value in stocks_1_sorted.items():
    print(f"Name: {key} | Price: {value}")

# ===== Stocks2 ======

stocks_2 = {}
num_stocks_set2 = 15
for i in range(num_stocks_set2):
    stocks_2[f"stock{i}"] = 100 * random.randint(1,50)
    print(f"stock{i}: {stocks_2[f"stock{i}"]}")

stocks_2_sorted = dict(sorted(stocks_2.items(),key = lambda x: x[1]))
for key,value in stocks_2_sorted.items():
    print(f"Name: {key} | Price: {value}")

unique_to_stocks1 = set(stocks_1.keys()) - set(stocks_2.keys())
print("=" * 10)
print(f"Stocks unique to stocks1 are: {unique_to_stocks1}")

# ==== common stocks ====
common_stocks = set(stocks_1.keys()) & set(stocks_2.keys())
print(f"Common Stocks: {common_stocks}")


price_mismatch_stocks = []
for stock in common_stocks:
    if stocks_1[stock] != stocks_2[stock]:
        price_mismatch_stocks.append(stock)

print(f"Stocks with price mismatch: {price_mismatch_stocks}")

# ==== remove duplicate prices from stocks_1 ====

unique_price_dict = {}
seen_prices = set()

for stock, price in stocks_1.items():
    if price not in seen_prices:
        unique_price_dict[stock] = price
        seen_prices.add(price)

print("="*10)
print("Stocks after removing duplicate prices:")
for k,v in unique_price_dict.items():
    print(k,v)


# ==== group stocks_1 by price ranges of 500 ====

grouped = {}

for stock, price in stocks_1.items():
    lower = (price // 500) * 500
    upper = lower + 499
    key = f"{lower}-{upper}"

    grouped.setdefault(key, []).append(stock)

print("="*10)
print("Grouped stocks (range of 500):")
for k, v in grouped.items():
    print(k, v)


stocks1_800 = [s for s, p in stocks_1.items() if p == 800]
stocks2_800 = [s for s, p in stocks_2.items() if p == 800]

print("="*10)
print("Stocks in stocks_1 with price 800:", stocks1_800)
print("Stocks in stocks_2 with price 800:", stocks2_800)