from dataclasses import dataclass, field

from builder.popo.OrderBook import OrderBook


@dataclass
class BuildOrderBookOutput:

    _orderBook: OrderBook | None = None

    @property
    def orderBook(self):
        return self._orderBook
    
    @orderBook.setter
    def orderBook(self, orderBook: OrderBook):
        self._orderBook = orderBook

