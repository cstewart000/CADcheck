import sys
import os
# print(sys.path)
sys.path.insert(0, os.getcwd() +"\\model\\")
cwd = os.getcwd() 

import unittest

from tool import Tool
from stock import Stock
from part import Part
from operation import Operation
from operation_type_enum import OperationType
from gcode import GCode
from shapely.geometry import Polygon
from cadFile import CadFile

class SetLayers(unittest.TestCase):

    def test_set_layers(self):
        model = CadFile(cwd + "\\resources\\test dxf files\\non_conformance_layers.dxf")
        model.auto_assign_layers()
        self.assertEqual(1,1)
       
if __name__ =='__main__':
    unittest.main()
