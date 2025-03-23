from builder.popo.Side import Side
from builder.popo.dto.BuildSideInput import BuildSideInput
from builder.popo.dto.BuildSideOutput import BuildSideOutput

"""
class to build a side
"""
class SideBuilder:
    
    @staticmethod
    def buildSide(buildSideInput: BuildSideInput) -> BuildSideOutput:
        assert buildSideInput is not None, "buildSideInput cannot be null"
        assert buildSideInput.sideString is not None, "sideString cannot be null"
        print(f"Receive buildSide request for buildSideInput: {buildSideInput}")

        sideString = buildSideInput.sideString
        if sideString == "BID":
            side = Side.BID
        elif sideString == "ASK":
            side = Side.ASK
        else:
            raise ValueError(f"Invalid sideString: {sideString}")
        print(f"Successfully construct side: {side}")

        buildSideOutput = BuildSideOutput()
        buildSideOutput.side = side
        print(f"Successfully construct buildSideOutput: {buildSideOutput}")

        return buildSideOutput
        