from builder.popo.Side import Side

"""
class to build a side
"""
class SideBuilder:
    
    @staticmethod
    def buildSide(sideString: str):
        if sideString == "BUY":
            return Side.BUY
        elif sideString == "SELL":
            return Side.SELL
        else:
            raise ValueError("Side String must be `BUY` or `SELL`")