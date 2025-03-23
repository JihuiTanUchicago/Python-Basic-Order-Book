from dataclasses import dataclass

from builder.popo.Side import Side

"""
class to represent an order
"""
@dataclass
class Order:
    
    _price: float
    _quantity: int
    _side: Side #BUY or SELL
    
    @property
    def price(self):
        return self._price
    
    @property
    def quantity(self):
        return self._quantity
    
    @property
    def side(self):
        return self._side
