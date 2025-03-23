from dataclasses import dataclass

from builder.popo.Order import Order

"""
dto class to build an order
"""
@dataclass
class BuildOrderOutput:
    
    _order: Order | None = None

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, order):
        self._order = order