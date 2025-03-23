from dataclasses import dataclass

"""
dto class to build an order
"""
@dataclass
class RemoveOrderInput:
    _id: str | None = None

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
