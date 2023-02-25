import os
import sys

sys.path.insert(0, os.getcwd() +"\\model\\")
sys.path.insert(0, os.getcwd() +"\\helper\\")

import ezdxf

from pathlib import Path
from shapely.geometry import Polygon
from shapely.geometry import Point
import math
from nesting import Nest
from nesting import Part


class cad_file:
    def __init__(self, filepath):
        self.filepath = filepath
        self.doc = ezdxf.readfile(filepath)    
    
    def write_to_file(self, save_path=None):
        if save_path is None:
            save_path = Path.home() / "Documents" / Path(self.filepath).name
        self.doc.saveas(save_path)

    def polyline_contains_polyline(self, polyline1, polyline2):
        shapely_polyline1 = Polygon(polyline1.get_points())
        shapely_polyline2 = Polygon(polyline2.get_points())
        return shapely_polyline1.contains(shapely_polyline2)

    def delete_duplicate_polylines(self):
        msp = self.doc.modelspace()
        polylines = msp.query('LWPOLYLINE') #+ msp.query('LWPOLYLINE') + msp.query('ACDBPOLYLINE')
        polylines_to_delete = []
        for e1 in polylines:
            for e2 in polylines:
                if e1 == e2:
                    continue
                if self.polyline_contains_polyline(e1, e2):
                    polylines_to_delete.append(e2)
            polylines = [p for p in polylines if p not in polylines_to_delete]
        return polylines

    def set_layers(self):
        msp = self.doc.modelspace()
        # Set layer for circles
        for e in msp.query('CIRCLE'):
            e.dxf.layer = "DRILL"
            e.dxf.color = 1 # Red color

        # Set layer for text
        for e in msp.query('TEXT'):
            e.dxf.layer = "ENGRAVE"
            e.dxf.color = 4 # Orange color
        # Set layer for mtext
        for e in msp.query('MTEXT'):
            e.dxf.layer = "ENGRAVE"
            e.dxf.color = 4 # Orange color
        
        polylines = msp.query('LWPOLYLINE')
        depths = self.assign_polyline_depth(polylines)
        self.set_layers_polylines(depths)

    def set_layers_three(self):
        msp = self.doc.modelspace()
        # Set layer for circles
        for e in msp.query('CIRCLE'):
            e.dxf.layer = "DRILL"
            e.dxf.color = 1 # Red color

        # Set layer for text
        for e in msp.query('TEXT'):
            e.dxf.layer = "ENGRAVE"
            e.dxf.color = 4 # Orange color
        # Set layer for mtext
        for e in msp.query('MTEXT'):
            e.dxf.layer = "ENGRAVE"
            e.dxf.color = 4 # Orange color
        
        #polylines = self.delete_duplicate_polylines()
        polylines = msp.query('LWPOLYLINE')
        # Set initial layer and color for remaining polylines
        for e in polylines:
            print(e)
            e.dxf.layer = "PROFILE"
            e.dxf.color = 3 # Yellow color
        
        # Set layer for enclosing polyline
        enclosing_polyline = None
        for e1 in polylines:
            is_enclosing = True
            for e2 in polylines:
                if e1 == e2:
                    continue
                if not self.polyline_contains_polyline(e1, e2):
                    is_enclosing = False
                    break
            if is_enclosing:
                enclosing_polyline = e1
                break
        
        if enclosing_polyline:
            enclosing_polyline.dxf.layer = "STOCKed"
            enclosing_polyline.dxf.color = 5 # Blue color
            #enclosing_polyline.dxf.linetype 

    def set_layers_two(self):
        msp = self.doc.modelspace()
        # Set layer for circles
        for e in msp.query('CIRCLE'):
            e.dxf.layer = "DRILL"
            e.dxf.color = 1 # Red color

        # Set layer for text
        for e in msp.query('TEXT'):
            e.dxf.layer = "ENGRAVE"
            e.dxf.color = 4 # Orange color
        # Set layer for mtext
        for e in msp.query('MTEXT'):
            e.dxf.layer = "ENGRAVE"
            e.dxf.color = 4 # Orange color
        
        #polylines = self.delete_duplicate_polylines()
        polylines = msp.query('LWPOLYLINE')
        # Set initial layer and color for remaining polylines
        for e in polylines:
            e.dxf.layer = "PROFILE INTERNAL"
            e.dxf.color = 3 # Yellow color
        depths = self.assign_polyline_depth(polylines)
        print(depths)        

    def write_to_file(self, save_path=None):
        if save_path is None:
            save_path = Path.home() / "Documents" / Path(self.filepath).name
        self.doc.saveas(save_path)

    def polyline_contains_polyline(self, polyline1, polyline2):
        points1 = [(x, y) for x, y, s, e, b in polyline1.get_points()]
        if not polyline1.closed:
            points1.append(points1[0])
        shapely_polyline1 = Polygon(points1)

        points2 = [(x, y) for x, y, s, e, b in polyline2.get_points()]
        if not polyline2.closed:
            points2.append(points2[0])
        shapely_polyline2 = Polygon(points2)

        return shapely_polyline1.contains(shapely_polyline2)

    def polyline_contains_point(self, polyline, point):
        points1 = [(x, y) for x, y, s, e, b in polyline.get_points()]
        if not polyline.closed:
            points1.append(points1[0])
        shapely_polyline = Polygon(points1)
        shapely_point = Point(point[0],point[1])

        return shapely_polyline.contains(shapely_point)

    def delete_duplicate_polylines(self):
        msp = self.doc.modelspace()
        polylines = msp.query('LWPOLYLINE') #+ msp.query('LWPOLYLINE') + msp.query('ACDBPOLYLINE')
        polylines_to_delete = []
        for e1 in polylines:
            for e2 in polylines:
                if e1 == e2:
                    continue
                if self.polyline_contains_polyline(e1, e2):
                    polylines_to_delete.append(e2)
            polylines = [p for p in polylines if p not in polylines_to_delete]
        return polylines

    def assign_polyline_depth(self, polylines):
        depths = {}
        for i, polyline1 in enumerate(polylines):
            depth = 1
            for j, polyline2 in enumerate(polylines):
                if i == j:
                    continue
                if self.polyline_contains_polyline(polyline2, polyline1):
                    depth += 1
            depths[polyline1] = depth
        return depths     

    def set_layers_polylines(self, depths):
        stock_layer = "STOCK"
        external_layer = "PROFILE EXTERNAL"
        internal_layer = "PROFILE INTERNAL"
        stock_color = 5 # Blue color
        external_color = 3 # Yellow color
        internal_color = 6 # Green color
        for polyline, depth in depths.items():
            if depth == 1:
                if self.is_rectangular(polyline):
                    polyline.dxf.layer = stock_layer
                    polyline.dxf.color = stock_color
                else:
                    polyline.dxf.layer = external_layer
                    polyline.dxf.color = external_color
            elif depth % 2 == 0:
                polyline.dxf.layer = internal_layer
                polyline.dxf.color = internal_color
            else:
                polyline.dxf.layer = external_layer
                polyline.dxf.color = external_color
    
    def is_rectangular(self, polyline):
        # check if the polyline is rectangular
        points = [(x, y) for x, y, s, e, b in polyline.get_points()]
        if not polyline.closed:
            points.append(points[0])
        shapely_polyline = Polygon(points)
        
        #shapely_polyline.area == shapely_polyline.minimum_rotated_rectangle

        return shapely_polyline.area == shapely_polyline.minimum_rotated_rectangle
    
    def add_dogbones_to_polylines(self, threshold_angle=135, offset=0.1, radius=0.1):
        msp = self.doc.modelspace()
        polylines = msp.query('LWPOLYLINE')
        for polyline in polylines:
            self.add_dogbone(polyline, threshold_angle, offset, radius)
    
    def get_parts(self):
        
        msp = self.doc.modelspace()
        polylines = msp.query('LWPOLYLINE')

        shapely_polylines = []

        for polyline in polylines:
            points = [(x, y) for x, y, s, e, b in polyline.get_points()]
            if not polyline.closed:
                points.append(points[0])
            shapely_polyline = Polygon(points)
            shapely_polylines.append(shapely_polyline)

        return shapely_polylines 

    def nest_parts(self, polylines, stock):

        parts = []
        for polyline in polylines:
            part = Part(polyline)
            parts.append(part)

        nest = Nest
        print(nest.nest_parts(self,parts,stock))
        


    def add_dogbone(self, polyline, threshold_angle, offset, radius):
        
        # Get the points of the polyline
        points = [(x, y) for x, y, s,e,b in polyline.get_points()]
        if not polyline.closed:
            points.append(points[0])
            
        
        print(points)

        threshold_angle = math.radians(threshold_angle)
        for i, point in enumerate(points):
            # Get the angle between the arms of the polyline
            prev_point = points[i-1]
            next_point = points[(i+1) % len(points)]
            angle = math.atan2(next_point[1]-point[1], next_point[0]-point[0]) - math.atan2(prev_point[1]-point[1], prev_point[0]-point[0])
            angle = math.atan2(prev_point[1]-point[1], prev_point[0]-point[0]) + math.atan2(next_point[1]-point[1], next_point[0]-point[0])
            
            print("point number: {}".format(i))
            print("point: {}".format(point))
            print("prev_point: {}".format(prev_point))
            print("next_point: {}".format(next_point))
            
            print(angle)

            if angle < -math.pi:
                angle += 2 * math.pi
            elif angle > math.pi:
                angle -= 2 * math.pi

            print(angle)

            # Check if the angle is less than the threshold
            if abs(angle) < threshold_angle:
                # Create the arc
                center = (point[0] + offset * math.cos(angle/2), point[1] + offset * math.sin(angle/2))
                
                end_angle = math.atan2(prev_point[1]-center[1], prev_point[0]-center[0])*180/math.pi
                start_angle = math.atan2(next_point[1]-center[1], next_point[0]-center[0])*180/math.pi
                
                
                mid_angle = start_angle+(end_angle-start_angle)/2
                mid_angle_rad = mid_angle*math.pi/180

                point_int_1 = [center[0]+radius*math.cos(mid_angle_rad),center[1]+radius*math.sin(mid_angle_rad)]
                point_int_2 = [center[0]-radius*math.cos(mid_angle_rad),center[1]-radius*math.sin(mid_angle_rad)]
                result = self.polyline_contains_point(polyline,point_int_1)
                arc_int_point = 0

                if result:
                    arc_int_point = self.doc.modelspace().add_point(point_int_1)
                    arc_int = self.doc.modelspace().add_arc(center, radius, start_angle, end_angle)
                    circle = self.doc.modelspace().add_circle(point_int_1, radius)   
                else:
                    arc_int_point = self.doc.modelspace().add_point(point_int_2)
                    arc_int = self.doc.modelspace().add_arc(center, radius, start_angle, end_angle)
                    circle = self.doc.modelspace().add_circle(point_int_2, radius)

                arc_int_point.dxf.layer = "DOGBONE_CEN"
                arc_int.dxf.layer = "DOGBONE_INT"         

                #arc_int.dxf.layer = "DOGBONE_INT"
                #arc_int_point = self.doc.modelspace().add_point(point_int_1)
                #
                #arc_ext.dxf.layer = "DOGBONE_EXT"

                print("center: {}".format(center))
                print("start_angle: {}".format(start_angle))
                print("end_angle: {}".format(end_angle))
                print("mid_angle: {}".format(mid_angle))
                print("arc_int_point: {}".format(arc_int_point))
                print("result: {}".format(result))

