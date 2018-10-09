class table:

    def __init__(self,attributes):
        self.attributes = attributes
        self.data = []
        
        self.keys = []
        for attribute in attributes:
            if attribute[1] == type("a"):
                self.keys.append(attribute)
        

    def add_record(self,record):
        



test = table([["id number",type("a")],["name",type("a")],["age",type(0)],["height",type(0.0)]])
