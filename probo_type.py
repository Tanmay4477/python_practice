from typing import TypedDict
from enum import Enum

class RequestType(Enum):
    BUY = "buy"
    SELL = "sell"

class StockType(Enum):
    YES = "yes"
    NO = "no"

class INRBalance(TypedDict):
    balance: int
    locked: int

INRData = dict[str, INRBalance]

class StockBalance(TypedDict):
    quantity: int
    locked: int

StockData = dict[str, dict[str, dict[StockType: StockBalance]]]

class Orders(TypedDict):
    userId: str
    type: str
    quantity: int
    orderId: int

class OrderOne(TypedDict):
    total: int
    orders: list[Orders]

OrderBookType = dict[str, dict[str, dict[str, OrderOne]]]