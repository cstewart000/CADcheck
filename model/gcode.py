import datetime

class GCode:
    def __init__(self, name, preamble, operations, conclusion, relative_path):
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.preamble = preamble
        self.operations = operations
        self.conclusion = conclusion
        self.relative_path = relative_path
    
    def write_to_file(self):
        filename = self.creation_date.strftime("%Y-%m-%d %H%Mhrs")+ " " + self.name + ".nc"
        filename = self.relative_path + '\\' + filename
        with open(filename, "w") as f:
            f.write(self.creation_date.strftime("%Y-%m-%d") + "\n")
            f.write(self.name + "\n")
            f.write("\n\n")
            f.write(self.preamble + "\n")
            f.write("\n\n")
            if isinstance(self.operations, list):
                for op in self.operations:
                    f.write(op.gcode + "\n")

            else:
               f.write(self.operations.gcode + "\n") 
        
            f.write("\n\n")
            f.write(self.conclusion + "\n")


    def write_each_operation_to_file(self):
        for i, op in enumerate(self.operations):
            filename = self.creation_date.strftime("%Y-%m-%d")[::-1] + "_" + self.name + "_" + str(i) + "_" + op + ".nc"
            with open(filename, "w") as f:
                f.write(self.creation_date.strftime("%Y-%m-%d") + "\n")
                f.write(filename + "\n")
                f.write("\n\n")
                f.write(self.preamble + "\n")
                f.write("\n\n")
                f.write(op + "\n")
                f.write("\n\n")
                f.write(self.conclusion + "\n")
    