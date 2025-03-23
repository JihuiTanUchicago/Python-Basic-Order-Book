from builder.popo.OrderBook import OrderBook
from builder.popo.dto.BuildOrderBookInput import BuildOrderBookInput
from builder.popo.dto.BuildOrderBookOutput import BuildOrderBookOutput 

from collections import OrderedDict, defaultdict

"""
class to build an order book
"""
class OrderBookBuilder:

    @staticmethod
    def buildOrderBook(buildOrderBookInput: BuildOrderBookInput) -> BuildOrderBookOutput:
        assert buildOrderBookInput is not None, "buildOrderBookInput cannot be null"
        assert buildOrderBookInput.symbol is not None and buildOrderBookInput.symbol != "", "symbol cannot be empty"
        print(f"Receive buildOrderBook request for buildOrderBookInput: {buildOrderBookInput}")

        symbol = buildOrderBookInput.symbol
        bidsPriceToOrderMap = buildOrderBookInput.bidsPriceToOrderMap
        asksPriceToOrderMap = buildOrderBookInput.asksPriceToOrderMap
        bidsPriceHeap = buildOrderBookInput.bidsPriceHeap
        asksPriceHeap = buildOrderBookInput.asksPriceHeap

        if bidsPriceToOrderMap is None:
            bidsPriceToOrderMap = defaultdict(OrderedDict)
        if asksPriceToOrderMap is None:
            asksPriceToOrderMap = defaultdict(OrderedDict)
        if bidsPriceHeap is None:
            bidsPriceHeap = []
        if asksPriceHeap is None:
            asksPriceHeap = []

        orderBook = OrderBook(symbol, bidsPriceToOrderMap, bidsPriceHeap, \
                              asksPriceToOrderMap, asksPriceHeap)
        print(f"Successfully construct orderBook: {orderBook}")

        buildOrderBookOutput = BuildOrderBookOutput()
        buildOrderBookOutput.orderBook = orderBook
        print(f"Successfully construct buildOrderBookOutput: {buildOrderBookOutput}")
        
        return buildOrderBookOutput