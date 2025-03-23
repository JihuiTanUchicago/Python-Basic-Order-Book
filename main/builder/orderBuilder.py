from builder.popo.Order import Order

"""
class to build an order
"""
class OrderBuilder:

    @staticmethod
    def buildOrder(price, quantity, side):
        return Order(price, quantity, side)