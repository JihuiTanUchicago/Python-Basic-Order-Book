from builder.popo.OrderBook import OrderBook
from builder.popo.Order import Order

from typing import Optional

"""
class to build an order book
"""
class OrderBookBuilder:

    @staticmethod
    def buildOrderBook(symbol: str, bids: Optional[Order], asks: Optional[Order]):
        return OrderBook(symbol, bids, asks)