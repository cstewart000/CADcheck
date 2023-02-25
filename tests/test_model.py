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
from shapely.geometry import Polygon

class TestModel(unittest.TestCase):


    def test_tool(self):
        tool = Tool('T10630')

        self.assertEqual(tool.diameter , 6)
        self.assertEqual(tool.length, 30)
        self.assertEqual(tool.type, '1')
        self.tool = tool

    def test_stock(self):

        stock = Stock(2440,1220,18)
        
        self.assertEqual(stock.stock_length , 2440)
        self.assertEqual(stock.stock_width, 1220)
        self.assertEqual(stock.depth, 18)

        self.stock = stock
    
    def test_part(self):
        part = Part(
            name="test_part",
            profile= Polygon([[0, 0], [300, 0], [300, 300], [0, 300]]),
            pockets= Polygon([[100, 100], [200, 100], [200, 200], [100, 200]]),
            internal_profiles= Polygon([[125, 125], [175, 125], [175, 175], [125, 175]]),
            holes= [[25,25],[25,275],[275,275],[275,25]],
            grain_direction_important=False,
            grain_direction_lengthwise=True)

        self.assertEqual(part.name, "test_part")
                
        self.part = part


if __name__ =='__main__':
    unittest.main()
