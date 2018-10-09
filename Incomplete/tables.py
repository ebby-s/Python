class table:

    def __init__(self,attributes):
        self.attributes = attributes
        self.data = []
        self.keys = []

    def add_record(self,record):
        key_gen = ""
        for i,field in enumerate(record):
            if self.attributes[i][1] != type(field):
                return False
            key_gen += str(field)
        
        key = hash(key_gen)
        self.data.append([key]+record)
        self.keys.append(key)
        return key

    def find_record(self,find_key):
        for i,key in enumerate(self.keys):
            if key == find_key:
                return self.data[i]



test = table([["name",type("a")],["age",type(0)],["height",type(0.0)]])
a = test.add_record(["Ebby",17,1.5])
b = test.add_record(["Sahil",17,1.6])
c = test.add_record(["Edmund",19,10.0])
