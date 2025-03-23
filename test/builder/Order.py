"""
class to represent an order
"""

class Order:
    def __init__(self, price, quantity, side):
        self.price = price
        self.quantity = quantity
        self.side = side
