import operator

class table:

    def __init__(self,attributes):
        self.attributes = []
        self.types = []
        for attribute in attributes:
            self.attributes.append(attribute[0])
            self.types.append(attribute[1])
        self.data = []
        self.operators = {"==":operator.eq,"<":operator.lt,">":operator.gt}

    def add_record(self,record):
        for i,field in enumerate(record):
            if self.types[i] != type(field):
                if type(field) == type(0) and self.types[i] == type(0.0):
                    record[i] = float(field)
                else:
                    return False
        
        self.data.append(record)

    def find_record(self,target_key):
        for record in self.data:
            if record[0] == target_key:
                return record

    def remove_record(self,target_key):
        for i,record in enumerate(self.data):
            if record[0] == target_key:
                del(self.data[i])

    def search(self,target_conditions):
        conditions = []
        for condition in target_conditions:
            condition = condition.split(" ")
            condition[0] = self.attributes.index(condition[0])
            condition[1] = self.operators[condition[1]]
            try:
                if self.types[condition[0]] == type(0):
                    condition[2] = int(condition[2])
                else:
                    condition[2] = float(condition[2])
            except:
                if condition[1] != self.operators["=="]:
                    continue
            conditions.append(condition)
        
        output = []
        for condition in conditions:
            for i,record in enumerate(self.data):
                if condition[1](record[condition[0]],condition[2]):
                    output.append(record)
        return output

test = table([["name",type("a")],["age",type(0)],["height",type(0.0)]])
test.add_record(["Ebby",17,1.5])
test.add_record(["Sahil",17,1.6])
test.add_record(["Edmund",19,2.5])
test.add_record(["Jeff",21,3.5])
print(test.search(["name == Sahil","age > 17"]))
