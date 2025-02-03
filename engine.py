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
        if self.inr_data.get(self.user_id) != self.user_id:
            self.inr_data[self.user_id] = { "balance": 0, "locked" : 0}
            self.write_data(self.inr_data, 'inr_balance.json')

        if self.stock_balance.get(self.user_id) != self.user_id:
            self.stock_balance[self.user_id] = {}
            self.write_data(self.stock_balance, 'stock_balance.json')
        
        if self.stock_balance[self.user_id].get(self.stock_symbol) != self.stock_symbol:
            self.stock_balance[self.user_id][self.stock_symbol] = {}
            self.write_data(self.stock_balance, 'stock_balance.json')

        if self.stock_balance[self.user_id][self.stock_symbol].get(self.stock_type) != self.stock_type:
            self.stock_balance[self.user_id][self.stock_symbol][self.stock_type] = { "quantity": 0, "locked": 0 }
            self.write_data(self.stock_balance, 'stock_balance.json')
        
        if self.orderbook.get(self.stock_symbol) != self.stock_symbol:
            self.orderbook[self.stock_symbol] = {}
            self.write_data(self.orderbook, 'orderbook.json')

        if self.orderbook[self.stock_symbol].get(self.stock_type) != self.stock_type:
            self.orderbook[self.stock_symbol][self.stock_type] = {}
            self.write_data(self.orderbook, 'orderbook.json')

        if self.orderbook[self.stock_symbol][self.stock_type].get(self.stock_price) != self.stock_price:
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
            json.dump(data, file)


    def buySomething(self) -> str:
        if self.inr_data[self.user_id]["balance"] < int(self.stock_quantity) * int(self.stock_price):
            raise ValueError("Low balance")
            
        if self.orderbook[self.stock_symbol][self.stock_type][self.stock_price].total < int(self.stock_quantity):
            raise ValueError("Low quantity, quantity not available")
        
        self.inr_data[self.user_id]["balance"] -= int(self.stock_quantity) * int(self.stock_price)
        self.orderbook[self.stock_symbol][self.stock_type][self.stock_price].total -= int(self.stock_quantity)
        self.stock_balance[self.user_id][self.stock_symbol][self.stock_type].quantity += int(self.stock_quantity)
        
        print("Order Successful")
        return
    
    def sellSomething(self) -> str:
        return