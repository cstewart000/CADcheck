import ezdxf
import shapely.geometry

class PolylineConverter:
    @staticmethod
    def shapely_to_ezdxf(shapely_polyline):
        dxf = ezdxf.new('R2010')
        model_space = dxf.modelspace()
        polyline = model_space.add_polyline2d(list(shapely_polyline.coords))
        return polyline

    @staticmethod
    def ezdxf_to_shapely(ezdxf_polyline):
        shapely_polyline = shapely.geometry.LineString([point for point in ezdxf_polyline])
        return shapely_polyline
