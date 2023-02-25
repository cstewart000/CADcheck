import sys
import os
# print(sys.path)
sys.path.insert(0, os.getcwd() +"\\model\\")

import unittest

from tool import Tool
from stock import Stock
from part import Part
from operation import Operation
from operation_type_enum import OperationType
from gcode import GCode
from shapely.geometry import Polygon

class TestGcode(unittest.TestCase):

    def test_operations(self):
        tool = Tool('T10630')
        stock = Stock(2440,1220,18)
  
        part = Part(
            name="test_part",
            profile= Polygon([[0, 0], [300, 0], [300, 300], [0, 300]]),
            pockets= Polygon([[100, 100], [200, 100], [200, 200], [100, 200]]),
            internal_profiles= Polygon([[125, 125], [175, 125], [175, 175], [125, 175]]),
            holes= [[25,25],[25,275],[275,275],[275,25]],
            grain_direction_important=False,
            grain_direction_lengthwise=True)

        operation = Operation(part.profile, OperationType.PROFILE_EXT, tool, stock.depth, 6, stock.depth)
        gcode = GCode("Test Gcode", "Preamble", operation, "Conclusion", "./resources/gcode_output/")
        gcode.write_to_file()
        self.assertEquals(gcode.name, "Test Gcode")
       
if __name__ =='__main__':
    unittest.main()
