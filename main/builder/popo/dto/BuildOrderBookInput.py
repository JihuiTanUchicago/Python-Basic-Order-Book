from dataclasses import dataclass, field
from collections import OrderedDict, defaultdict

from builder.popo.Order import Order


@dataclass
class BuildOrderBookInput:

    _symbol : str | None = None
    _bidsPriceToOrderMap: dict[float, OrderedDict[str, list[Order]]] = \
        field(default_factory=lambda: defaultdict(OrderedDict))
    _asksPriceToOrderMap: dict[float, OrderedDict[str, list[Order]]] = \
        field(default_factory=lambda: defaultdict(OrderedDict))
    _bidsPriceHeap : list[float] = field(default_factory=list)
    _asksPriceHeap : list[float] = field(default_factory=list)

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
    
    @symbol.setter
    def symbol(self, symbol):
        self._symbol = symbol

    @bidsPriceToOrderMap.setter
    def bidsPriceToOrderMap(self, bidsPriceToOrderMap):
        self._bidsPriceToOrderMap = bidsPriceToOrderMap

    @asksPriceToOrderMap.setter
    def asksPriceToOrderMap(self, asksPriceToOrderMap):
        self._asksPriceToOrderMap = asksPriceToOrderMap

    @bidsPriceHeap.setter
    def bidsPriceHeap(self, bidsPriceHeap):
        self._bidsPriceHeap = bidsPriceHeap

    @asksPriceHeap.setter
    def asksPriceHeap(self, asksPriceHeap):
        self._asksPriceHeap = asksPriceHeap

    

