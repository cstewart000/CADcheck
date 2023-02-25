from cad_file import cad_file
import ezdxf
import shapely

#model = cad_file(r"C:\\Users\\Cameron.Stewart\\Documents\\GitHub\\d-i-ply products\\open to suggestions\\models\\Open to suggestion (short v2)_1 direct.dxf")
model = cad_file(r"C:\\Users\\Cameron.Stewart\\Documents\\GitHub\\CADcheck\\test dxf files\\dev_dogbone2.dxf")
#model = cad_file(r"C:\\Users\\Cameron.Stewart\\Documents\\GitHub\\CADcheck\\test dxf files\\dev_nested_plines.dxf")

#model.set_layers()
model.add_dogbones_to_polylines(135,0,20)
model.write_to_file()
