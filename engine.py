from probo_type import INRData, StockData, OrderBookType
import json

class Engine: 

    def __init__(self, stock_type, stock_price, stock_quantity, stock_symbol, user_id):
        self.stock_type = stock_type
        self.stock_price = stock_price
        self.stock_quantity = stock_quantity
        self.stock_symbol = stock_symbol
        self.user_id = user_id

        self.orderbook: OrderBookType
        self.stock_balance: StockData
        self.inr_data: INRData
        self.openData()
        self.updatingData()
        
    
    def updatingData(self):
        if self.user_id not in self.inr_data:
            self.inr_data[self.user_id] = { "balance": 0, "locked" : 0}
            self.write_data(self.inr_data, 'inr_balance.json')

        if self.user_id not in self.stock_balance:
            self.stock_balance[self.user_id] = {}
            self.write_data(self.stock_balance, 'stock_balance.json')
        
        if self.stock_symbol not in self.stock_balance[self.user_id]:
            self.stock_balance[self.user_id][self.stock_symbol] = {}
            self.write_data(self.stock_balance, 'stock_balance.json')

        if self.stock_type not in self.stock_balance[self.user_id][self.stock_symbol]:
            self.stock_balance[self.user_id][self.stock_symbol][self.stock_type] = { "quantity": 0, "locked": 0 }
            self.write_data(self.stock_balance, 'stock_balance.json')
        
        if self.stock_symbol not in self.orderbook:
            self.orderbook[self.stock_symbol] = {}
            self.write_data(self.orderbook, 'orderbook.json')

        if self.stock_type not in self.orderbook[self.stock_symbol]:
            self.orderbook[self.stock_symbol][self.stock_type] = {}
            self.write_data(self.orderbook, 'orderbook.json')

        if self.stock_price not in self.orderbook[self.stock_symbol][self.stock_type]:
            self.orderbook[self.stock_symbol][self.stock_type][self.stock_price] = { "total": 0, "orders": []}
            self.write_data(self.orderbook, 'orderbook.json')
        
        

    def openData(self):
        try:
            with open('orderbook.json', "r") as file1:
                self.orderbook = json.load(file1)

            with open('stock_balance.json', "r") as file2:
                self.stock_balance = json.load(file2)
            
            with open('inr_balance.json', "r") as file3:
                self.inr_data = json.load(file3)
        except FileNotFoundError:
            print("File not found")
    
    def write_data(self, data, filename):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)


    def buySomething(self) -> str:
        if self.inr_data[self.user_id]["balance"] < int(self.stock_quantity) * float(self.stock_price):
            raise ValueError("Low balance")
            
        if self.orderbook[self.stock_symbol][self.stock_type][self.stock_price]["total"] < int(self.stock_quantity):
            raise ValueError("Low quantity, quantity not available")
        
        quantity = int(self.stock_quantity)

        self.orderbook[self.stock_symbol][self.stock_type][self.stock_price]["total"] -= quantity
        self.inr_data[self.user_id]["balance"] -= quantity * float(self.stock_price)
        self.stock_balance[self.user_id][self.stock_symbol][self.stock_type]["quantity"] += quantity

        for x in self.orderbook[self.stock_symbol][self.stock_type][self.stock_price]["orders"]:

            if x["type"] == "normal":
                self.inr_data[x["userId"]]["balance"] += int(self.stock_quantity) * float(self.stock_price)

            if x["quantity"] >= quantity:
                x["quantity"] -= quantity
                break
            else:
                quantity -= x["quantity"]
                x["quantity"] = 0
                    
        self.write_data(self.orderbook, 'orderbook.json')
        self.write_data(self.stock_balance, 'stock_balance.json')
        self.write_data(self.inr_data, 'inr_balance.json')
        print("Order Successful")
        return
    
    def sellSomething(self) -> str:
        if self.stock_balance[self.user_id][self.stock_symbol][self.stock_type]["quantity"] < int(self.stock_quantity):
            raise ValueError("Low quantity of stocks, you cannot buy this much stocks")
        
        self.stock_balance[self.user_id][self.stock_symbol][self.stock_type]["quantity"] -= int(self.stock_quantity)
        self.stock_balance[self.user_id][self.stock_symbol][self.stock_type]["locked"] += int(self.stock_quantity)
        self.orderbook[self.stock_symbol][self.stock_type][self.stock_price]["total"] += int(self.stock_quantity)
        self.orderbook[self.stock_symbol][self.stock_type][self.stock_price]["orders"].append({"userId": self.user_id, "type": "normal", "quantity": int(self.stock_quantity)})

        self.write_data(self.orderbook, 'orderbook.json')
        self.write_data(self.stock_balance, 'stock_balance.json')

        print("Sell Order in process, sold successfully")
        return
