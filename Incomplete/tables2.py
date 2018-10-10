class table:

    def __init__(self,attributes):
        self.attributes = attributes
        self.data = []

    def add_record(self,record):
        for i,field in enumerate(record):
            if self.attributes[i][1] != type(field):
                if type(field) == type(0) and self.attributes[i][1] == type(0.0):
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
        operators = [" = "," > "," < "]
        for condition in target_conditions:
            

        output = self.data

        for condition in conditions:
            for record in output:
                if record


test = table([["name",type("a")],["age",type(0)],["height",type(0.0)]])
test.add_record(["Ebby",17,1.5])
test.add_record(["Sahil",17,1.6])
test.add_record(["Edmund",19,2.5])
test.add_record(["Jeff",21,3.5])
