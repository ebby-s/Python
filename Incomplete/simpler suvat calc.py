import operator

class Stack:                 # Stack for evaluating postfix
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return (self.items == [])

def input_values():     # Inputs values for suvat, x is the value to be found
    inputs = {"s":None,"u":None,"v":None,"a":None,"t":None}
    for key in inputs.keys():
        value = str(input("Input value for {0}(or x to find): ".format(key)))
        if value == '': value = None
        inputs[key] = value
    return inputs

def choose_equation(values):      # Chooses an equation depending on values present
    if None in values.values():
        return equations[list(values.keys())[list(values.values()).index(None)]]

def sub_values(equation,values):        # Substitutes value for all instances of variable name in equation
    for key in values.keys():
        if values[key] is not None: equation = equation.replace(key,values[key])
    return equation

def evaluate(token_list):           # Simplies by evaluating postfix
    stack = Stack()
    operators = {"+":operator.add,"-":operator.sub,"*":operator.mul,"^":operator.pow}
    for token in token_list:
        if token in operators.keys():
            operand2 = stack.pop()
            operand1 = stack.pop()
            try: stack.push(operators[token](float(operand1),float(operand2)))
            except: stack.push("("+str(operand1)+token+str(operand2)+")")
        else: stack.push(token)
    return stack.items

no_s = "v u a t * + ="
no_u = "s v t * 0.5 a * t 2 ^ * - ="
no_v = "s u t * 0.5 a * t 2 ^ * + ="
no_a = "s 0.5 t * u v + * ="
no_t = "v 2 ^ u 2 ^ a s * 2 * + = "

equations = {"s":no_s,"u":no_u,"v":no_v,"a":no_a,"t":no_t}

values = input_values()
while "x" not in values.values():
    print("You need to enter 'x' for the value you want to calculate")
    values = input_values()

equation = choose_equation(values)
print(equation)
equation = sub_values(equation,values)
print(equation)
simplified = evaluate(equation.split(" "))
print(simplified)
