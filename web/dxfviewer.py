import ezdxf

class DXFViewer:
    def __init__(self, file):
        self.file = file
        self.data = self.parse_dxf()

    def parse_dxf(self):
        dxf = ezdxf.readfile(self.file)
        modelspace = dxf.modelspace()
        lines = []
        for e in modelspace:
            if e.dxftype() == 'LINE':
                lines.append((e.dxf.start, e.dxf.end))
        return lines
