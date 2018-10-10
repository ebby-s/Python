class table:

    def __init__(self,attributes):
        self.attributes = attributes
        self.data = []
        self.keys = []

    def add_record(self,record):
        key_gen = ""
        for i,field in enumerate(record):
            if self.attributes[i] != type(field):
                if type(field) == type(0) and self.attributes[i] == type(0.0):
                    record[i] = float(field)
                else:
                    return False
            key_gen += str(field)
        
        key = hash(key_gen)
        self.data.append([key]+record)
        self.keys.append(key)
        return key

    def find_record(self,target_key):
        for i,key in enumerate(self.keys):
            if key == target_key:
                return self.data[i][1:]

    def remove_record(self,target_key):
        for i,key in enumerate(self.keys):
            if key == target_key:
                del(self.data[i])
                del(self.keys[i])


test = table([type("a"),type(0),type(0.0)])
a = test.add_record(["Ebby",17,1.5])
b = test.add_record(["Sahil",17,1.6])
c = test.add_record(["Edmund",19,2.5])
d = test.add_record(["Jeff",21,3.5])
