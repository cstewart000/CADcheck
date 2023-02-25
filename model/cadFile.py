
import ezdxf

class CadFile:
    def __init__(self, path):
        self.dwg = ezdxf.readfile(path)
        self.modelspace = self.dwg.modelspace()

    def set_layer(self, entities, layer, color, elevation=0.0, line_type='CONTINUOUS'):
        for entity in entities:
            entity.dxf.layer = layer
            entity.dxf.color = color
            entity.dxf.elevation = elevation

            if str(entity.dxf._entity)[0:6] != 'CIRCLE':
                entity.dxf.line_type = line_type
            

    def get_polylines(self):
        return self.modelspace.query('POLYLINE')

    def get_circles(self):
        return self.modelspace.query('CIRCLE')

    def write_to_file(self, path):
        self.dwg.saveas(path)

    def dog_bone_polyline(self, polyline, length):
        pass

    def auto_assign_layers(self):
        circles = self.get_circles()
        small_circles = [circle for circle in circles if circle.dxf.radius <= 5.0]
        self.set_layer(small_circles, 'DRILL', 1)
