import operator
# This program is for entertainment purposes only, do not try at home.

class Tree:             # Node for building trees
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.cargo)

def is_float(value):           # Returns true if value can be converted to float
    try:
        value = float(value)
        return True
    except:
        return False

def root(number,exponent):           # Returns root of value
    return number**(1/exponent)

def print_tree(tree):            # Prints tree, for debugging
    if tree is None: return
    print_tree(tree.left)
    print(tree.cargo, end=" ")
    print_tree(tree.right)

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

def add_numbers(equation,values):     # Substitutes values into equation
    for key in values.keys():
        equation = substitute(equation,[key,values[key]])
    return equation

def substitute(tree,value):        # Substitutes value for all instances of variable name in equation
    if tree is None: return
    tree.right = substitute(tree.right,value)
    tree.left = substitute(tree.left,value)
    if tree.cargo == value[0] and value[1] != None: tree.cargo = value[1]
    return tree

def contains_x(tree):                    # Checks if x is in branch
    if tree.cargo == "x": return True
    if tree.right != None:
        if contains_x(tree.right): return True
    if tree.left != None:
        if contains_x(tree.left): return True
    return False

def simplify(tree):                   # Solves some of the tree                            POLYNOMIALS???
    operators = {"+":operator.add,"-":operator.sub,"*":operator.mul,"^":operator.pow}
    if tree.left != None and tree.right != None:
        if is_float(tree.right.cargo) and is_float(tree.left.cargo):
            tree.cargo = operators[tree.cargo](float(tree.left.cargo),float(tree.right.cargo))
            tree.left = None
            tree.right = None
    if tree.right != None: tree.right = simplify(tree.right)
    if tree.left != None: tree.left = simplify(tree.left)
    return tree

# SUVAT equations as trees
no_s = Tree("=",Tree("v"),Tree("+",Tree("u"),Tree("*",Tree("a"),Tree("t"))))                                                             # v = u + a * t
no_u = Tree("=",Tree("s"),Tree("-", Tree("*",Tree("v"),Tree("t")), Tree("*",Tree("*",Tree(0.5),Tree("a")),Tree("^",Tree("t"),Tree(2))))) # s = vt - 0.5*at^2
no_v = Tree("=",Tree("s"),Tree("+", Tree("*",Tree("u"),Tree("t")), Tree("*",Tree("*",Tree(0.5),Tree("a")),Tree("^",Tree("t"),Tree(2))))) # s = ut + 0.5*at^2
no_a = Tree("=",Tree("s"),Tree("*",Tree("*",Tree(0.5),Tree("t")),Tree("+",Tree("u"),Tree("v"))))                                         # s = 0.5*(u+v)t
no_t = Tree("=",Tree("^",Tree("v"),Tree(2)),Tree("+",Tree("^",Tree("u"),Tree(2)),Tree("*",Tree("*",Tree("a"),Tree("s")),Tree(2))))       # v^2 = u^2 + 2as

equations = {"s":no_s,"u":no_u,"v":no_v,"a":no_a,"t":no_t}

values = input_values()
while "x" not in values.values():
    print("You need to enter 'x' for the value you want to calculate")
    values = input_values()

equation = choose_equation(values)
print_tree(equation)
print()
equation = add_numbers(equation,values)
print_tree(equation)
print()
print(contains_x(equation.left),contains_x(equation.right))

print_tree(simplify(equation.left))
print_tree(simplify(equation.right))



