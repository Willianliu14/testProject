import csv

filename = "stock_data.csv"
stock_prices = [
    ("AAPL", "Apple", [145, 148, 147, 150, 155]),
    ("GOOGL", "Alphabet", [2800, 2825, 2810, 2850, 2900]),
    ("TSLA", "Tesla", [700, 720, 710, 730, 750])
]

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["股票代码", "股票名称", "收盘价"])
    for stock in stock_prices:
        writer.writerow([stock[0], stock[1], ",".join(map(str, stock[2]))])

stocks = {}
with open(filename, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        code, name, prices_str = row
        prices = list(map(float, prices_str.split(",")))
        stocks[code] = (name, prices)

returns = {}
for code, (name, prices) in stocks.items():
    daily_returns = [(prices[i] - prices[i - 1]) / prices[i - 1] for i in range(1, len(prices))]
    returns[code] = daily_returns

print("\n 股票日收益率分析：")
for code, daily_returns in returns.items():
    print(f"\n {stocks[code][0]} ({code})")
    for i, r in enumerate(daily_returns, 1):
        print(f"  第 {i} 天收益率: {r:.2%}")
