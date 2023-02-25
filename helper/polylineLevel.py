from typing import List
from shapely.geometry import Polygon, MultiPolygon
# https://chat.openai.com/chat/520f97ca-9571-46d9-8f24-e198ea4327bb


class PolylineLevel:
    @staticmethod
    def polyline_encloses(polyline1, polyline2):
        poly1 = Polygon(polyline1)
        poly2 = Polygon(polyline2)
        if poly1.contains(poly2):
            return polyline1
        elif poly2.contains(poly1):
            return polyline2
        else:
            return None

    @staticmethod
    def get_depth(polylines: List[List[tuple]]):
        depth_dict = {}
        for i, polyline1 in enumerate(polylines):
            depth = 0
            for j, polyline2 in enumerate(polylines):
                if i == j:
                    continue
                if PolylineLevel.polyline_encloses(polyline1, polyline2):
                    depth += 1
            depth_dict[tuple(polyline1)] = depth
        return depth_dict
    
    @staticmethod
    def is_rectangle(polyline: List[tuple]):
        poly = Polygon(polyline)
        if not poly.is_valid or poly.area <= 0 or poly.length != 4:
            return False
        x_coords = set([p[0] for p in polyline])
        y_coords = set([p[1] for p in polyline])
        return len(x_coords) == 2 and len(y_coords) == 2
    
    @staticmethod
    def assign_layers(polylines: List[List[tuple]]):
        depth_dict = PolylineLevel.get_depth(polylines)
        layers = {}
        stock = None
        for polyline in polylines:
            if PolylineLevel.is_rectangle(polyline):
                width = max(polyline, key=lambda x: x[0])[0] - min(polyline, key=lambda x: x[0])[0]
                height = max(polyline, key=lambda x: x[1])[1] - min(polyline, key=lambda x: x[1])[1]
                if width < 2500 and height < 1300:
                    stock = polyline
            if stock is not None:
                if depth_dict[tuple(polyline)] == 0:
                    layers[tuple(polyline)] = "stock"
                elif depth_dict[tuple(polyline)] % 2 == 1:
                    layers[tuple(polyline)] = "external"
                else:
                    layers[tuple(polyline)] = "internal"
            else:
                if depth_dict[tuple(polyline)] % 2 == 0:
                    layers[tuple(polyline)] = "external"
                else:
                    layers[tuple(polyline)] = "internal"
        return layers