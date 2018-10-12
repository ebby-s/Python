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
                elif self.types[condition[0]] == type(0.0):
                    condition[2] = float(condition[2])
            except:
                if condition[1] != self.operators["=="]:
                    continue
            conditions.append(condition)
        
        output = self.data.copy()
        for condition in conditions:
            for i,record in enumerate(self.data):
                if not condition[1](record[condition[0]],condition[2]):
                    if record in output:
                        output.remove(record)
        return output

test = table([["name",type("a")],["cores",type(0)],["threads",type(0)],["frequency",type(0.0)]])
test.add_record(['1200',4,4,3.1])
test.add_record(['1300X',4,4,3.4])
test.add_record(['1400',4,8,3.2])
test.add_record(['1500X',4,8,3.5])
test.add_record(['1600',6,12,3.2])
test.add_record(['1600X',6,12,3.6])
test.add_record(['1700',8,16,3.0])
test.add_record(['1700X',8,16,3.4])
test.add_record(['1800X',8,16,3.6])
print(test.search(["cores > 4","frequency > 3.0"]))
