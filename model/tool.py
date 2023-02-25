class Tool:
    def __init__(self, ID):
        self.ID = ID

        if(len(ID)==6):
            self.type = ID[1]
            self.diameter = int(ID[2:4])
            self.length = int(ID[4:6])
            self.pocket_number = 0
        
        self.flutes = 0
        self.comment = ""

    def __str__(self):
        return "ID: {}, Type: {}, Diameter: {}, Length: {}, Flutes: {}".format(self.ID, self.type, self.diameter, self.length, self.flutes)

def toolloader(filepath):
    tools = []
    with open(filepath, "r") as f:
        for line in f:
            data = line.split(";")
            if len(data) == 2:
                comment = data[1]
            tool_number, pocket_number, diameter = data[0].split(" ")
            tool = Tool(tool_number)
            tool.pocket_number = pocket_number
            tool.comment = comment
            tools.append(tool)

    return tools  


#tool_list = toolloader("tools2.tbl")
#print(tool_list)
