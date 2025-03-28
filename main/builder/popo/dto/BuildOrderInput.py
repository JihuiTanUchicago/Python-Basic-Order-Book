from dataclasses import dataclass

from builder.popo.Side import Side

"""
dto class to build an order
"""
@dataclass
class BuildOrderInput:
    _id: str | None = None
    _price: float | None = None
    _quantity: int | None = None
    _side: Side | None = None #BUY or SELL

    @property
    def id(self):
        return self._id
    
    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity
    
    @property
    def side(self):
        return self._side
    
    @id.setter
    def id(self, id):
        self._id = id
        
    @price.setter
    def price(self, price):
        self._price = price
    
    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity
    
    @side.setter
    def side(self, side):
        self._side = side
