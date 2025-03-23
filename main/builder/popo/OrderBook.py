from dataclasses import dataclass, field

from builder.popo.Order import Order
from builder.popo.Side import Side


"""
class to represent an order book
here we implement the Time-Price priority 
L3 order book
"""
@dataclass
class OrderBook:
    
    _symbol : str
    _bids : list[Order] = field(default_factory=list) # Max-heap (Negative Prices)
    _asks : list[Order] = field(default_factory=list) # Min-heap (Normal Prices)

    @property
    def symbol(self):
        return self._symbol

    @property
    def bids(self):
        return self._bids

    @property
    def asks(self):
        return self._asks

