import xml.etree.ElementTree as ET

class Config:
    def __int__(self):
        pass

    def initialise(self,gcode_preamble, gcode_conclusion, stock_length, stock_width, stock_depth, contour_tool, dog_boning_tool, drill_tools):
        
        self.gcode_preamble = gcode_preamble
        self.gcode_conclusion =gcode_conclusion
        self.stock_length = stock_length
        self.stock_width = stock_width
        self.stock_depth = stock_depth
        self.contour_tool = contour_tool
        self.dog_boning_tool = dog_boning_tool
        self.drill_tools = drill_tools

    def init_from_xml(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        self.gcode_preamble = root.find('python_object').find('gcode_preamble').text
        self.gcode_conclusion = root.find('python_object').find('gcode_conclusion').text   
        self.stock_length = int(root.find('python_object').find('stock_length').text)
        self.stock_width = int(root.find('python_object').find('stock_width').text)
        self.stock_depth = float(root.find('python_object').find('stock_depth').text)
        self.contour_tool = root.find('python_object').find('contour_tool').text
        self.dog_boning_tool = root.find('python_object').find('dog_boning_tool').text
        self.drill_tools = [drill.text for drill in root.find('python_object').find('drill_tools').findall('drill')]

        