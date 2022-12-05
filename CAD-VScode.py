
"""
Written: cstewart000@gmail.com
 6 june 2022

https://ezdxf.readthedocs.io/en/stable/
"""

import sys
import ezdxf
import shapely
from ezdxf.addons import geo
from shapley.geometry import shape


def readFile(filename):

    try:
        doc = ezdxf.readfile(filename)
        msp = doc.modelspace()
        return doc
    except IOError:
        print(f"Not a DXF file or a generic I/O error.")
        sys.exit(1)
    except ezdxf.DXFStructureError:
        print(f"Invalid or corrupted DXF file.")
        sys.exit(2)
    
    
def testGaps(doc):
    
    print(f"Test gaps")
    msp = doc.modelspace()
    lines = msp.query("LWPOLYLINE")
    for line in lines:
        if line is None:
            print(f"No lwpolylines in model - test passed")

        # print(line.closed)
        if not line.closed:
            return False
        else:
            return True

def fixGaps(doc):
    
    print(f"Close gaps")
    
    msp = doc.modelspace()
    lines = msp.query("LWPOLYLINE")
    for line in lines:
        if line is None:
            print(f"No lwpolylines in model - test passed")

        # print(line.closed)
        if not line.closed:
            line.closed = True
        
    return doc


def testElevation(doc):
    
    print(f"Test elevation")
    msp = doc.modelspace()
    lines = msp.query("LWPOLYLINE")
    for line in lines:
        if line is None:
            print(f"No lwpolylines in model - test passed")

        # print(line.closed)
        if line.dxf.elevation == 0 :
            return True
        else:
            return False

        
def fixElevation(doc):
    
    print(f"fix elevations")
    
    msp = doc.modelspace()
    lines = msp.query("LWPOLYLINE")
    for line in lines:
        if line is None:
            print(f"No lwpolylines in model - test passed")

        # print(line.closed)
        if line.dxf.elevation != 0 :
            line.dxf.elevation = 0

    return doc


def findRange(doc):
    
    # TODO: implement a bounding box geom class
    xMin= None
    xMax=None
    yMin=None
    yMax =None
    
    print(f"Test range")
    msp = doc.modelspace()
    lines = msp.query("LWPOLYLINE")
    for line in lines:
        if line is None:
            print(f"No lwpolylines in model - test passed")

        # print(line.closed)
        for point in line:
            if(xMin == None):
                xMin= point[0]
                xMax= point[0]
                yMin=point[1]
                yMax = point[1]
                
            else:      
                if point[0]< xMin:
                    xMin = point[0]
                if point[0] > xMax: 
                    xMax = point[0]
                if point[1] < yMin:
                    yMin = point[1]
                if point[1] < xMax:
                    xMax = point[1]

    return [xMin, yMin, xMax, yMax]
                

def testRange(doc):
    docRange = findRange(doc)

    if(docRange[0] > 0 and
       docRange[1] > 0 and
       docRange[2] < 2400 and
       docRange[3] < 1200):
        return True
    else:
        return False
       

def fixRange(doc):
    
    print(f"fix range")
    
    msp = doc.modelspace()
    lines = msp.query("LWPOLYLINE")
    for line in lines:
        if line is None:
            print(f"No lwpolylines in model - test passed")

        # print(line.closed)
        if line.dxf.elevation != 0 :
            line.dxf.elevation = 0

    return doc

def fixLayers(doc):
    
        
    print(f"Test layers")
    msp = doc.modelspace()
    
    #for layer in doc.layers:
    #if layer.dxf.name != "0"
    
    circles = msp.query("CIRCLE")
    for circle in circles:
        diameter = circle.dxf.radius*2
        
        if diameter<=8:
            
            circle.dxf.layer = "DRILL_"+str(diameter)
            
        else:
            circle.dxf.layer = "PROFILE_INT"

    plines = msp.query("LWPOLYLINE")
    
    for pline in plines:
        if pline.dxf.elevation == 0:
           pline.dxf.layer = "PROFILE" 
        
        else:
            pocket_depth = 18.2 - pline.dxf.elevation
            pline.dxf.layer = "POCKET_"+str(pocket_depth)
            
    return doc


def fixLayersNested(doc):
    
        
    print(f"Fix Nested")
    msp = doc.modelspace()

    plines = msp.query("LWPOLYLINE")
    
    for pline in plines:
        pline_proxy = geo.proxy(pline)
        
        
        if pline.dxf.elevation == 0:
           pline.dxf.layer = "PROFILE" 
        
        else:
            pocket_depth = 18.2 - pline.dxf.elevation
            pline.dxf.layer = "POCKET_"+str(pocket_depth)
            
    return doc