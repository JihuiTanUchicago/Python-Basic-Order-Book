from dataclasses import dataclass

from builder.popo.OrderBook import OrderBook
from builder.popo.Order import Order
from builder.popo.Side import Side
from builder.orderbookBuilder import OrderBookBuilder
from builder.orderBuilder import OrderBuilder
from builder.sideBuilder import SideBuilder

@dataclass
class ExchangeComponent:
    _exchangeName: str
    _orderBookMap: dict[str, OrderBook] # symbol -> OrderBook
