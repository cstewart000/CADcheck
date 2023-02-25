import sys
import os
# print(sys.path)
sys.path.insert(0, os.getcwd() +"\\model\\")
sys.path.insert(0, os.getcwd() +"\\helper\\")

import unittest

from config import Config

class TestConfig(unittest.TestCase):

    def test_config(self):
        config = Config()
        config.init_from_xml(os.getcwd() + "\\configuration\\config.xml")
        print(config)
        self.assertEqual(config.stock_length, 2440)
        self.assertEqual(config.stock_width, 1220)
        self.assertEqual(config.stock_depth, 18.2)
       
  


if __name__ =='__main__':
    unittest.main()
