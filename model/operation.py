import shapely.geometry as geometry
from operation_type_enum import OperationType
import math

class Operation:
    def __init__(self, geometry: geometry, type: str, tool: str, stock_depth: float, step_down_depth: float, final_depth: float):
        self.geometry = geometry
        self.type = type
        self.tool = tool
        self.stock_depth = stock_depth
        self.toolpath = None
        self.step_down_depth = step_down_depth
        self.final_depth = final_depth
        self.gcode = ""
        self.generate_toolpath()

    def __str__(self):
        return f'Type: {self.type}, Tool: {self.tool}, Stock Depth: {self.stock_depth}, Step Down Depth: {self.step_down_depth}, Final Depth: {self.final_depth}'

    def generate_toolpath(self):
        if self.type == OperationType.PROFILE_INT:
            # Generate internal contour toolpath
            pass
        elif self.type == OperationType.PROFILE_EXT:
            self.toolpath = self.geometry.buffer(self.tool.diameter / 2)

            for step in range(math.ceil(self.stock_depth/self.step_down_depth)):
                           
                z_height = self.stock_depth - self.step_down_depth*step 
                if z_height < 0:
                    z_height = 0
                self.gcode += generate_gcode(self.toolpath, [0,0], 30, z_height)
            
        elif self.type == 'pocket':
            # Generate pocket toolpath
            pass
        elif self.type == 'drill':
            # Generate drill toolpath
            pass
        elif self.type == 'engrave':
            # Generate engrave toolpath
            pass


def generate_gcode(geometry: geometry, start_point: tuple, safe_height_z: float, feed_height_z: float) -> str:
        gcode = ''
        #if isinstance(geometry, geometry.Point):
        #    # Move to start point
        #    gcode += f'G0 X{start_point[0]} Y{start_point[1]} Z{safe_height_z}\n'
            # Move to geometry point - plunge
        #    gcode += f'G0 X{geometry.x} Y{geometry.y} Z{feed_height_z}\n'
        #elif isinstance(geometry, geometry.LineString):
        #    # Move to start point
        #    gcode += f'G0 X{start_point[0]} Y{start_point[1]} Z{safe_height_z}\n'
        #    # Cut along line - plunge
        #    for point in geometry.coords:
        #        gcode += f'G1 X{point[0]} Y{point[1]}\n'
        #elif isinstance(geometry, geometry.Polygon):
            # Move to start point
        gcode += f'G0 X{format(start_point[0], ".4g")} Y{format(start_point[1], ".4g")} Z{format(feed_height_z, ".4g")}\n'
            # Cut along exterior boundary - plunge
        for point in geometry.exterior.coords:
            gcode += f'G1 X{format(point[0], ".4g")} Y{format(point[1], ".4g")} Z{feed_height_z, ".4g"}\n'
            # Cut along interior boundaries
        #    for interior in geometry.interiors:
        #        for point in interior.coords:
        #            gcode += f'G1 X{point[0]} Y{point[1]}\n'
        #else:
        #    raise ValueError('Unsupported geometry type')
        return gcode
