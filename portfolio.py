import csv

# Sample current prices (from S&P 500 dataset idea)
current_prices = {
    "AAPL": 220.5,
    "GOOGL": 175.2,
    "MSFT": 430.0,
    "TSLA": 250.75,
    "AMZN": 195.4
}

portfolio = {}

print("=== Stock Portfolio Tracker ===")
print("Available tickers:", list(current_prices.keys()))

n = int(input("How many stocks do you want to add? "))

for i in range(n):
    ticker = input(f"\nEnter ticker {i+1} (e.g. AAPL): ").upper()
    buy_price = float(input(f"Enter buy price for {ticker}: "))
    shares = int(input(f"Enter number of shares for {ticker}: "))
    portfolio[ticker] = {"buy_price": buy_price, "shares": shares}

print("\n--- Portfolio Summary ---")
total_invested = 0
total_current = 0

rows = []

for ticker, data in portfolio.items():
    buy_price = data["buy_price"]
    shares = data["shares"]
    invested = buy_price * shares
    current_price = current_prices.get(ticker, buy_price)
    current_value = current_price * shares
    gain_loss = current_value - invested
    gain_pct = (gain_loss / invested * 100) if invested != 0 else 0

    print(f"{ticker}: Invested Rs.{invested:.2f} | Current Rs.{current_value:.2f} | Gain/Loss: {gain_pct:.2f}%")

    total_invested += invested
    total_current += current_value
    rows.append([ticker, buy_price, shares, invested, current_price, current_value, round(gain_pct, 2)])

print(f"\nTotal Invested: Rs.{total_invested:.2f}")
print(f"Total Current Value: Rs.{total_current:.2f}")
print(f"Total Gain/Loss: Rs.{total_current - total_invested:.2f}")

# Save to CSV
with open("portfolio_summary.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Ticker", "Buy Price", "Shares", "Invested", "Current Price", "Current Value", "Gain %"])
    writer.writerows(rows)

print("\nSaved to portfolio_summary.csv")
