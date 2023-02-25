import shapely.geometry

class Stock:
    def __init__(self):
        self.parts = []
        self.drill_for_hold_downs = []
        self.stock_length = 0
        self.stock_width = 0
        self.stock_outline = shapely.geometry.Polygon()
        self.depth = 0

    def __init__(self, length, width, depth):
        self.stock_length = length
        self.stock_width = width
        self.depth = depth
        self.stock_outline = shapely.geometry.Polygon([(0,0), (0,width), (length,width), (length,0)])

    def set_stock_dimensions(self, length, width, depth):
        self.stock_length = length
        self.stock_width = width
        self.depth = depth
        self.stock_outline = shapely.geometry.Polygon([(0,0), (0,width), (length,width), (length,0)])

