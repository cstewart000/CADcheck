import sys
import os

cwd = os.getcwd() 

sys.path.insert(0, cwd +"\\model\\")
sys.path.insert(0,cwd +"\\helper\\")
sys.path.insert(0, cwd)

from cad_file import cad_file
import ezdxf
import shapely

model = cad_file(cwd + "\\resources\\test dxf files\\dev_nested.dxf")

#model.set_layers()
stock = shapely.Polygon([(0,0),(2400,0),(2400,1200),(0,1200), (0,0)])

part_outlines = model.get_parts()


#model.nest_parts(part_outlines,stock)


model.write_to_file()
