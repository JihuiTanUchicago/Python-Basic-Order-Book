from dataclasses import dataclass
from collections import OrderedDict
from typing import Optional
import heapq

from component.pojo.dto.AddOrderInput import AddOrderInput
from component.pojo.dto.AddOrderOutput import AddOrderOutput
from component.pojo.dto.ModifyOrderInput import ModifyOrderInput
from component.pojo.dto.ModifyOrderOutput import ModifyOrderOutput
from component.pojo.dto.RemoveOrderInput import RemoveOrderInput
from component.pojo.dto.RemoveOrderOutput import RemoveOrderOutput

from builder.popo.OrderBook import OrderBook
from builder.popo.Order import Order
from builder.popo.Side import Side
from builder.orderbookBuilder import OrderBookBuilder
from builder.orderBuilder import OrderBuilder
from builder.sideBuilder import SideBuilder

@dataclass
class ExchangeComponent:
    _name: str # Name of the Exchange, e.g. NYSE, NASDAQ, etc.
    _orderBookMap: dict[str, OrderBook] # symbol -> OrderBook
    _idToOrderMap: dict[str, Order] # id -> Order

    @property
    def name(self):
        return self._name

    @property
    def orderBookMap(self):
        return self._orderBookMap
    
    @property
    def priceToOrderMap(self):
        return self._priceToOrderMap
    
    @orderBookMap.setter
    def orderBookMap(self, orderBookMap):
        self._orderBookMap = orderBookMap
    
    @priceToOrderMap.setter
    def priceToOrderMap(self, priceToOrderMap):
        self._priceToOrderMap = priceToOrderMap

    # Check and execute a match if bids and asks cross
    def tryMatch(self, order: Order) -> Optional[Order]:
        # Get Order Book
        orderBook = self.orderBookMap.get(order.symbol)
        if orderBook is None:
            raise ValueError(f"Order Book with symbol: {order.symbol} does not exist")

        # Attempt to find Match and Execute Match
        if order.side == Side.BID:
            oppositePriceToOrderMap = orderBook.asksPriceToOrderMap
            oppositePriceHeap = orderBook.bidsPriceHeap
            sign = 1
        elif order.side == Side.ASK:
            oppositePriceToOrderMap = orderBook.bidsPriceToOrderMap
            oppositePriceHeap = orderBook.asksPriceHeap
            sign = -1
        else:
            raise ValueError(f"Invalid side: {order.side}")
        
        while len(oppositePriceHeap) != 0 and order.price * sign >= oppositePriceHeap[0] and order.quantity > 0:
            # check if priceHeap[0] does not have corresponding orders
            if abs(oppositePriceHeap[0]) not in oppositePriceToOrderMap or len(oppositePriceToOrderMap[abs(oppositePriceHeap[0])]) == 0:
                heapq.heappop(oppositePriceHeap)
                continue

            oppositePrice = abs(oppositePriceHeap[0])
            oppositeOrders = oppositePriceToOrderMap[oppositePrice]
            oppositeOrder = next(iter(oppositeOrders))
            if oppositeOrder.quantity > order.quantity:
                oppositeOrder.quantity -= order.quantity
                order.quantity = 0
            else:
                order.quantity -= oppositeOrder.quantity
                oppositeOrder.quantity = 0
                del oppositePriceToOrderMap[oppositePrice][oppositeOrder.id]
                if len(oppositePriceToOrderMap[oppositePrice]) == 0:
                    del oppositePriceToOrderMap[oppositePrice]
                    heapq.heappop(oppositePriceHeap)
        
        print(f"Last Traded Price: {order.price}")
        if order.quantity > 0:
            return order
        return None




    def addOrder(self, addOrderInput: AddOrderInput) -> AddOrderOutput:
        assert addOrderInput is not None, "addOrderInput cannot be null"
        assert addOrderInput.id is not None, "order id cannot be null"
        assert addOrderInput.price is not None, "price cannot be null"
        assert addOrderInput.quantity is not None, "quantity cannot be null"
        assert addOrderInput.side is not None, "side cannot be null"
        print(f"Receive addOrder request for addOrderInput: {addOrderInput}")

        # Build the incoming Add Order
        id, price, quantity, side = addOrderInput.id, addOrderInput.price, \
            addOrderInput.quantity, addOrderInput.side
        order = Order(id, price, quantity, side)
        print(f"Successfully construct order: {order}")

        # Check if it matches an opposite order
        order = self.tryMatch(order)
        if order == None:
            addOrderOutput = AddOrderOutput()
            addOrderOutput.success = True
            return addOrderOutput
        
        # Get Corresponding Order Book
        symbol = addOrderInput.symbol
        orderBook = self.orderBookMap.get(symbol)
        if orderBook is None:
            orderBook = OrderBookBuilder.buildOrderBook(symbol)
            self.orderBookMap[symbol] = orderBook

        # Update Order Book
        if side == Side.BID:
            priceToOrderMap = orderBook.bidsPriceToOrderMap
            priceHeap = orderBook.bidsPriceHeap
        else:
            priceToOrderMap = orderBook.asksPriceToOrderMap
            priceHeap = orderBook.asksPriceHeap

        if price not in priceToOrderMap:
            priceToOrderMap[price] = OrderedDict()
            sign = 1 if side == Side.BID else -1
            heapq.heappush(priceHeap, price * sign)
        priceToOrderMap[price][id] = order

        # Update idToOrderMap
        self.idToOrderMap[id] = order

        # Construct Add Order Output
        addOrderOutput = AddOrderOutput()
        addOrderOutput.success = True

        print(f"Successfully construct addOrderOutput: {addOrderOutput}")
        return addOrderOutput

    def removeOrder(self, removeOrderInput: RemoveOrderInput) -> RemoveOrderOutput:
        assert removeOrderInput is not None, "removeOrderInput cannot be null"
        assert removeOrderInput.id is not None, "order id cannot be null"
        print(f"Receive removeOrder request for removeOrderInput: {removeOrderInput}")

        order = self.idToOrderMap.get(removeOrderInput.id)
        if order is None:
            raise ValueError(f"Order with id: {removeOrderInput.id} does not exist")
        
        # Get Corresponding Order Book
        symbol = order.symbol
        orderBook = self.orderBookMap.get(symbol)
        if orderBook is None:
            raise ValueError(f"Order Book with symbol: {symbol} does not exist")

        # Update Order Book
        if order.side == Side.BID:
            priceToOrderMap = orderBook.bidsPriceToOrderMap
            priceHeap = orderBook.bidsPriceHeap
        else:
            priceToOrderMap = orderBook.asksPriceToOrderMap
            priceHeap = orderBook.asksPriceHeap

        # Update priceToOrderMap
        if order.price not in priceToOrderMap:
            raise ValueError(f"Order with price: {order.price} does not exist")
        if order.id not in priceToOrderMap[order.price]:
            raise ValueError(f"Order with id: {order.id} does not exist")
        price, id = order.price, order.id
        del priceToOrderMap[price][id]
        if len(priceToOrderMap[price]) == 0:
            del priceToOrderMap[price]

        # Update idToOrderMap
        del self.idToOrderMap[id]

        # Construct RemoveOrderOutput
        removeOrderOutput = RemoveOrderOutput()
        removeOrderOutput.success = True

        print(f"Successfully construct removeOrderOutput: {removeOrderOutput}")
        return removeOrderOutput

    def modifyOrder(self, modifyOrderInput: ModifyOrderInput) -> ModifyOrderOutput:
        assert modifyOrderInput is not None, "modifyOrderInput cannot be null"
        assert modifyOrderInput.id is not None, "order id cannot be null"
        assert modifyOrderInput.price is not None or modifyOrderInput.quantity is not None, \
            "price or quantity cannot be both null"
        print(f"Receive modifyOrder request for modifyOrderInput: {modifyOrderInput}")

        # Get Order
        order = self.idToOrderMap.get(modifyOrderInput.id)
        if order is None:
            raise ValueError(f"Order with id: {modifyOrderInput.id} does not exist")

        if modifyOrderInput.price is not None and modifyOrderInput.price != order.price:
            print("Price changed, removing old order and adding new order")
            self.removeOrder(RemoveOrderInput(modifyOrderInput.id))
            newQuantity = order.quantity if modifyOrderInput.quantity is None else modifyOrderInput.quantity
            self.addOrder(AddOrderInput(modifyOrderInput.id, order.symbol,
                                        modifyOrderInput.price, newQuantity,
                                        modifyOrderInput.side))
        elif modifyOrderInput.quantity is not None and modifyOrderInput.quantity != order.quantity:
            print("Price unchanged, but quantity changed")

            # Update idToOrderMap
            newOrder = Order(order.id, order.price, modifyOrderInput.quantity, order.side)
            self.idToOrderMap[id] = newOrder

            # Update Order Book
            symbol = order.symbol
            orderBook = self.orderBookMap.get(symbol)
            if orderBook is None:
                raise ValueError(f"Order Book with symbol: {symbol} does not exist")

            if order.side == Side.BID:
                priceToOrderMap = orderBook.bidsPriceToOrderMap
            else:
                priceToOrderMap = orderBook.asksPriceToOrderMap

            # Update priceToOrderMap
            if order.price not in priceToOrderMap:
                raise ValueError(f"Order with price: {order.price} does not exist")
            if order.id not in priceToOrderMap[order.price]:
                raise ValueError(f"Order with id: {order.id} does not exist")
            price, id = order.price, order.id
            # if quantity is less, do not change it's priority
            # if quantity is more, add to last of the queue
            if modifyOrderInput.quantity > order.quantity:
                del priceToOrderMap[price][id]
                priceToOrderMap[price][id] = newOrder
            else:
                priceToOrderMap[price][id] = newOrder

        # Construct ModifyOrderOutput
        modifyOrderOutput = ModifyOrderOutput()
        modifyOrderOutput.success = True

        print(f"Successfully construct modifyOrderOutput: {modifyOrderOutput}")
        return modifyOrderOutput

