
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 400
}

def main():
    print("            Stock Portfolio Tracker ")
    print(f"Available stocks in system: {', '.join(STOCK_PRICES.keys())}\n")
    
    total_portfolio_value = 0
    portfolio = []

    while True:
        ticker = input("Enter stock ticker (or type 'calculate' to finish): ").strip().upper()
        
        if ticker == 'CALCULATE':
            break
            
        if ticker in STOCK_PRICES:
            try:
                quantity = int(input(f"Enter quantity for {ticker}: "))
                if quantity < 0:
                    print("Quantity cannot be negative. Try again.\n")
                    continue
                
                price = STOCK_PRICES[ticker]
                investment_value = quantity * price
                total_portfolio_value += investment_value
                
                portfolio.append((ticker, quantity, price, investment_value))
                print(f"Added {quantity} shares of {ticker} (${investment_value:,}).\n")
                
            except ValueError:
                print("Invalid input. Please enter a whole number for quantity.\n")
        else:
            print(f"Error: Price for '{ticker}' is not available in our system. Please try again.\n")

    # Display final results
    print("\n")
    print("       PORTFOLIO SUMMARY       ")
    print("\n")
    
    if not portfolio:
        print("Your portfolio is currently empty.")
    else:
        for ticker, qty, price, total in portfolio:
            print(f"{ticker}: {qty} shares x ${price} = ${total:,}")
        
        print("="*35)
        print(f"TOTAL INVESTMENT VALUE: ${total_portfolio_value:,}")
    print("="*35)

if __name__ == "__main__":
    main()
