from dataclasses import dataclass

"""
dto class to build an order
"""
@dataclass
class ModifyOrderInput:
    _id: str | None = None
    _price: float | None = None
    _quantity: int | None = None

    @property
    def id(self):
        return self._id
    
    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity
    
    @id.setter
    def id(self, id):
        self._id = id
        
    @price.setter
    def price(self, price):
        self._price = price
    
    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity
