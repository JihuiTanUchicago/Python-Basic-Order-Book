from builder.popo.Order import Order
from builder.popo.dto.BuildOrderInput import BuildOrderInput
from builder.popo.dto.BuildOrderOutput import BuildOrderOutput

"""
class to build an order
"""
class OrderBuilder:

    @staticmethod
    def buildOrder(buildOrderInput: BuildOrderInput) -> Order:
        assert buildOrderInput is not None, "buildOrderInput cannot be null"
        assert buildOrderInput.price is not None, "price cannot be null"
        assert buildOrderInput.quantity is not None, "quantity cannot be null"
        assert buildOrderInput.side is not None, "side cannot be null"
        print(f"Receive buildOrder request for buildOrderInput: {buildOrderInput}")

        price, quantity, side = buildOrderInput.price, buildOrderInput.quantity, buildOrderInput.side
        order = Order(price, quantity, side)
        print(f"Successfully construct order: {order}")

        buildOrderOutput = BuildOrderOutput()
        buildOrderOutput.order = order
        print(f"Successfully construct builderOrderOutput: {buildOrderOutput}")

        return buildOrderOutput