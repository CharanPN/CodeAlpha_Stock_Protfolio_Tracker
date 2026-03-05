stock_info = {
    "AAPL" : 180,
    "TSLA" : 250,
    "GOOG" : 150,
    "MSFT" : 300,
    "AMZN" : 170,
    "NVDA" : 450,
    "META" : 320,
    "NFLX" : 400 
}

total_investment = 0
invested_stocks = {}

print("WELCOME TO CSE - Charan Stock Exchange".center(200,"-"))

while True:
    print("\nAvailable Stocks and it's Price :")
    for stock, price in stock_info.items():
        print(f"{stock} - ${price}")
    
    new_stock = input("\nEnter stock name : ").strip().upper()
    while new_stock not in stock_info:
        print(f"{new_stock} is not available")
        new_stock = input("Enter stock name form the above list : ").strip().upper()
    stock_quantity = int(input("Enter quantity : "))
    investment = stock_info[new_stock] * stock_quantity
    print(f"\nInvestment on {new_stock} is {investment}")
    total_investment += investment

    if new_stock in invested_stocks:
        add_stock = invested_stocks[new_stock]
        stock_quantity += add_stock[1]
        investment = stock_info[new_stock] * stock_quantity

    invested_stocks[new_stock] = [stock_info[new_stock], stock_quantity, investment]

    choice = input("\nAdd another stock? (yes/no) : ").strip().lower()
    if choice != "yes":
        print("Exiting...")
        break

with open("portfolio.txt", "w") as f:
    f.write("Portfolio")
    for stock_name, other_info in invested_stocks.items():
        f.write(f"\n\nStock name - {stock_name}")
        f.write(f"\nStock price - ${other_info[0]}")
        f.write(f"\nStock quantity - {other_info[1]}")
        f.write(f"\nInvestment - ${other_info[2]}")
    f.write(f"\n\nTotal investment - ${total_investment}")

print(f"\n\nTotal investment : {total_investment}")
print("Thank You For Using CSE".center(200,"-"))