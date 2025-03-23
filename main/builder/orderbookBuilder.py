from builder.popo.OrderBook import OrderBook
from builder.popo.Order import Order
from builder.popo.dto.BuildOrderBookInput import BuildOrderBookInput
from builder.popo.dto.BuildOrderBookOutput import BuildOrderBookOutput 

from typing import Optional

"""
class to build an order book
"""
class OrderBookBuilder:

    @staticmethod
    def buildOrderBook(buildOrderBookInput: BuildOrderBookInput) -> BuildOrderBookOutput:
        assert buildOrderBookInput is not None, "buildOrderBookInput cannot be null"
        assert buildOrderBookInput.symbol is not None and buildOrderBookInput.symbol != "", "symbol cannot be empty"
        print(f"Receive buildOrderBook request for symbol: {symbol}, bids: {bids}, asks: {asks}")

        symbol, bids, asks = buildOrderBookInput.symbol, buildOrderBookInput.bids, buildOrderBookInput.asks
        if bids is None:
            bids = []
        if asks is None:
            asks = []
        orderBook = OrderBook(symbol, bids, asks)
        print(f"Successfully construct orderBook: {orderBook}")

        buildOrderBookOutput = BuildOrderBookOutput()
        buildOrderBookOutput.orderBook = orderBook
        print(f"Successfully construct buildOrderBookOutput: {buildOrderBookOutput}")
        
        return buildOrderBookOutput