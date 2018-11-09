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

class Tree:             # Node for building trees
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def print_tree(tree):            # Prints tree, for debugging
    if tree is None: return
    print_tree(tree.left)
    print(tree.cargo, end=" ")
    print_tree(tree.right)

def add_numbers(equation,values):     # Substitutes values into equation
    for key in values.keys():
        equation = substitute(equation,[key,values[key]])
    return equation

def substitute(tree,value):        # Substitutes value for all instances of variable name in equation
    if tree is None: return
    tree.right = substitute(tree.right,value)
    tree.left = substitute(tree.left,value)
    if tree.cargo == value[0] and value[1] != None:
        tree.cargo = value[1]
    return tree

def tree_to_postfix(tree):     # Converts tree to postfix to solve
    global postfix
    if tree is None: return
    tree_to_postfix(tree.left)
    tree_to_postfix(tree.right)
    postfix += str(tree.cargo)+' '

def evaluate(token_list):           # Simplies by evaluating postfix
    stack = Stack()
    operators = {"+":operator.add,"-":operator.sub,"*":operator.mul,"^":operator.pow}
    for token in token_list:
        if token in operators.keys():
            operand2 = stack.pop()
            operand1 = stack.pop()
            try:
                stack.push(operators[token](float(operand1),float(operand2)))
            except:
                stack.push(str(operand1)+token+str(operand2))
        else:
            stack.push(token)
    return stack

# SUVAT equations as trees
no_s = Tree("=",Tree("v"),Tree("+",Tree("u"),Tree("*",Tree("a"),Tree("t")))) # v = u + a * t
no_u = Tree("=",Tree("s"),Tree("-", Tree("*",Tree("v"),Tree("t")), Tree("*",Tree("*",Tree(0.5),Tree("a")),Tree("^",Tree("t"),Tree(2))))) # s = vt - 0.5*at^2
no_v = Tree("=",Tree("s"),Tree("+", Tree("*",Tree("u"),Tree("t")), Tree("*",Tree("*",Tree(0.5),Tree("a")),Tree("^",Tree("t"),Tree(2))))) # s = ut + 0.5*at^2
no_a = Tree("=",Tree("v"),Tree("*",Tree("*",Tree(0.5),Tree("t")),Tree("+",Tree("u"),Tree("v")))) # v = 0.5*(u+v)t
no_t = Tree("=",Tree("^",Tree("v"),Tree(2)),Tree("+",Tree("^",Tree("u"),Tree(2)),Tree("*",Tree("*",Tree("a"),Tree("s")),Tree(2)))) # v^2 = u^2 + 2as

equations = {"s":no_s,"u":no_u,"v":no_v,"a":no_a,"t":no_t}

def input_values():     # Inputs values for suvat, x is the value to be found
    inputs = {"s":None,"u":None,"v":None,"a":None,"t":None}
    for key in inputs.keys():
        value = str(input("Input value for {0}(or x to find): ".format(key)))
        if value == '': value = None
        inputs[key] = value
    return inputs

def choose_equation(values):      # Chooses an equation depending on values present
    return equations[list(values.keys())[list(values.values()).index(None)]]



values = input_values()
equation = choose_equation(values)
equation = add_numbers(equation,values)
print_tree(equation)
postfix = ''
tree_to_postfix(equation)
print(postfix)
simplified = evaluate(postfix.split())
while not simplified.is_empty():
    print(simplified.pop())
