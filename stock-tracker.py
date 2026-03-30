# =========================
# Stock Portfolio Tracker
# =========================

# Hardcoded stock prices (USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 320,
    "AMZN": 3400
}

portfolio = {}

print("Welcome to Stock Portfolio Tracker\n")

# Taking user input
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    
    if stock == 'DONE':
        break
    
    if stock not in stock_prices:
        print("Stock not available in price list!\n")
        continue
    
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number!\n")

# Calculating total investment
print("\nYour Portfolio:")
total_value = 0

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} shares x ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Optional: Save to file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()

if save == 'yes':
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("------------------------\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares x ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print("Data saved to portfolio.txt")