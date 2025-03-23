from dataclasses import dataclass

from builder.popo.Side import Side
"""
Side of the order
"""
@dataclass
class BuildSideOutput():
    
    _side: Side | None = None

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, side):
        self._side = side