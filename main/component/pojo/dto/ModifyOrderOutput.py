from dataclasses import dataclass

"""
dto class to build an order
"""
@dataclass
class ModifyOrderOutput:
    _success: bool = False

    @property
    def success(self):
        return self._success
    
    @success.setter
    def success(self, success):
        self._success = success
