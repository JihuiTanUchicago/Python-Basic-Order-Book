from dataclasses import dataclass

"""
Side of the order
"""
@dataclass
class BuildSideInput():
    
    _sideString : str | None = None # Can be "Bid" or "Ask" ONLY

    @property
    def sideString(self):
        return self._sideString
    
    @sideString.setter
    def side(self, sideString):
        self._sideString = sideString