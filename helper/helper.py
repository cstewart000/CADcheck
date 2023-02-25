from shapely.geometry import *


def createContour(contourShapes, tool):
    tool_dia = 0.5
    offset_distance = tool_dia / 2

    # Create the offset
    offset = polygon.buffer(offset_distance)