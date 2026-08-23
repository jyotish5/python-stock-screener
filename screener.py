import csv

stocks_data = [
    {"symbol": "TATAMOTORS", "price": 980, "sma_20": 950},
    {"symbol": "RELIANCE", "price": 2900, "sma_20": 2950},
    {"symbol": "INFY", "price": 1500, "sma_20": 1420},
    {"symbol": "HDFCBANK", "price": 1450, "sma_20": 1480}
]

breakout_stocks = []
for stock in stocks_data:
    if stock["price"] > stock["sma_20"]:
        breakout_stocks.append([stock["symbol"], stock["price"], stock["sma_20"], "BUY"])

filename = "stock_signals.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Symbol", "Price", "20_SMA", "Signal"])
    writer.writerows(breakout_stocks)

print("Report generated successfully!")
