import shapely.geometry
from shapely.affinity import translate
from shapely.affinity import rotate

class Part:
    def __init__(self, outline):
        self.outline = outline
    
    def get_outline(self):
        return self.outline
    
    def transform(self, x, y, rotation):
        self.outline = rotate(self.outline, rotation)
        self.outline = translate(self.outline, x, y)

class Nest:

    def __init__(self):
        self


    def nest_parts(self, parts, polygon):
            
        """
        Nest a list of parts into a given polygon.
        """
        parts_to_place = list(parts)
        used_area = polygon
        placed_parts = []
        
        while parts_to_place:
            part = parts_to_place.pop()
            part_outline = part.get_outline()
            
            # Find the best location and rotation for the part
            best_location = None
            min_intersection = float("inf")
            nesting_iteration = 0
            for x in range(0, int(polygon.bounds[2] - part_outline.bounds[2]), 10):
                for y in range(0, int(polygon.bounds[3] - part_outline.bounds[3]), 10):
                    for rotation in [0, 90, 180, 270]:
                        rotated_outline = rotate(part_outline, rotation)
                        translated_outline = translate(rotated_outline, x, y)
                        intersection = used_area.intersection(translated_outline).area
                        if intersection < min_intersection:
                            min_intersection = intersection
                            best_location = (x, y, rotation)
            
                        nesting_iteration = nesting_iteration+1
                        print(nesting_iteration)
                        print(x)
                        print(y)
                        print(rotation)
                        
            # Place the part
            if best_location:
                part.transform(*best_location)
                used_area = used_area.difference(part.get_outline())
                placed_parts.append(part)
        
        return placed_parts




