from dataclasses import dataclass, field

from builder.popo.Order import Order


@dataclass
class BuildOrderBookInput:

    _symbol : str | None = None
    _bids : list[Order] | None = None # Max-heap (Negative Prices)
    _asks : list[Order] | None = None # Min-heap (Normal Prices)

    @property
    def symbol(self):
        return self._symbol

    @property
    def bids(self):
        return self._bids

    @property
    def asks(self):
        return self._asks
    
    @symbol.setter
    def symbol(self, symbol):
        self._symbol = symbol

    @bids.setter
    def bids(self, bids):
        self._bids = bids

    @asks.setter
    def asks(self, asks):
        self._asks = asks

