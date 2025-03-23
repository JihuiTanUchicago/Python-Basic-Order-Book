from dataclasses import dataclass, field
from collections import OrderedDict

from builder.popo.Order import Order


"""
class to represent an order book
here we implement the Time-Price priority 
L3 order book
"""
@dataclass
class OrderBook:
    
    _symbol : str
    _bidsPriceToOrderMap : dict[float, OrderedDict[str, list[Order]]]
    _bidsPriceHeap : list[float] = field(default_factory=list) # positive numbers for Min Heap
    _asksPriceToOrderMap : dict[float, OrderedDict[str, list[Order]]]
    _asksPriceHeap : list[float] = field(default_factory=list) # negative numbers for Max Heap

    @property
    def symbol(self):
        return self._symbol

    @property
    def bidsPriceToOrderMap(self):
        return self._bidsPriceToOrderMap

    @property
    def asksPriceToOrderMap(self):
        return self._asksPriceToOrderMap
    
    @property
    def bidsPriceHeap(self):
        return self._bidsPriceHeap

    @property
    def asksPriceHeap(self):
        return self._asksPriceHeap
    


