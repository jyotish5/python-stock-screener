import json

# Simulated Live Crypto Data
crypto_portfolio = [
    {"symbol": "BTC", "buy_price": 60000, "current_price": 63500},
    {"symbol": "ETH", "buy_price": 3200, "current_price": 2950},
    {"symbol": "SOL", "buy_price": 140, "current_price": 155},
    {"symbol": "DOGE", "buy_price": 0.15, "current_price": 0.11}  # Significant Drop
]

print("==========================================")
print("   CRYPTO RISK & ALERT MONITOR SYSTEM     ")
print("==========================================\n")

alerts = []

for coin in crypto_portfolio:
    symbol = coin["symbol"]
    buy = coin["buy_price"]
    current = coin["current_price"]
    
    # Percentage Change Calculation
    pnl_percent = ((current - buy) / buy) * 100
    
    if pnl_percent <= -5:
        status = "⚠️ CRITICAL ALERT: HIGH DROP!"
        alerts.append(f"{symbol} is down by {pnl_percent:.2f}%")
    elif pnl_percent > 0:
        status = "🟢 PROFITABLE"
    else:
        status = "⚪ NEUTRAL / MINOR LOSS"
        
    print(f"[{symbol}] Buy: ${buy} | Current: ${current} | PnL: {pnl_percent:.2f}% -> {status}")

print("\n------------------------------------------")
print(f"Total Risk Alerts Triggered: {len(alerts)}")
for alert in alerts:
    print(f"👉 {alert}")
