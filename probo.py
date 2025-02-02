from probo_type import RequestType, StockType
from engine import Engine
    
user_id: str = input("Put your user id: ")
buy_sell_type: RequestType = input("You want to buy or sell: ").lower()
stock_symbol: str = input("Please enter stock symbol: ").upper()
stock_quantity: int = int(input("Please enter the quantity: "))
stock_price: int = int(input("Please enter the price: "))
stock_type: StockType = input("Please enter the stock type: ").lower()

engine = Engine(stock_type, stock_price, stock_quantity, stock_symbol, user_id)

if(buy_sell_type == "buy"):
    print("you want to buy something")
    engine.buySomething()
else:
    print("you want to sell")
    engine.sellSomething()

