import operator,copy
# Yes there are simpler solutions BUT I LIKE TREES.

class Tree:             # Node for building trees
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.cargo)
    def __int__(self):
        return int(self.cargo)

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
    while True:
        inputs = {"s":None,"u":None,"v":None,"a":None,"t":None}
        for key in inputs.keys():
            value = str(input("Input value for {0}(or x to find): ".format(key)))
            if value == '': value = None
            inputs[key] = value
        if "x" in inputs.values():
            return inputs
        else:
            print("Invalid values entered")

def input_bulk():                 # Inputs a lot of values :D
    while True:
        try:
            repeats = int(input("Enter number of repeats: "))
            if repeats > 0: break
            else: print("Value has to be positive.")
        except: print("Value has to be an integer.")
    
    constants = input_values()
    inputs = [copy.deepcopy(constants) for x in range(repeats)]
    while True:
        variable = input("Enter variable: ")
        if variable in list('suvat'): break
        else: print("Variable has to be s,u,v,a, or t.")
    values = []
    while len(values) < repeats:
        try:
            value = float(input("Enter a value: "))
            values.append(value)
        except: print("Value has to be a float.")
    for i,value in enumerate(values):
        inputs[i][variable] = value
    return inputs

def choose_equation(values):      # Chooses an equation depending on values present
    if None in values.values():
        return copy.deepcopy(equations[list(values.keys())[list(values.values()).index(None)]])

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

def simplify(tree):                   # Solves some of the tree
    operators = {"+":operator.add,"-":operator.sub,"*":operator.mul,"^":operator.pow}
    if tree.left != None and tree.right != None:
        if is_float(tree.right.cargo) and is_float(tree.left.cargo):
            tree.cargo = operators[tree.cargo](float(tree.left.cargo),float(tree.right.cargo))
            tree.left = None
            tree.right = None
        if tree.cargo == "*" and tree.right.cargo == "*" and is_float(tree.left.cargo):
            if is_float(tree.right.right.cargo):
                tree.left.cargo = float(tree.left.cargo)*float(tree.right.right.cargo)
                tree.right = tree.right.left
            elif is_float(tree.right.left.cargo):
                tree.left.cargo = float(tree.left.cargo)*float(tree.right.left.cargo)
                tree.right = tree.right.right
        elif tree.cargo == "*" and tree.left.cargo == "*" and is_float(tree.right.cargo):
            if is_float(tree.left.right.cargo):
                tree.right.cargo = float(tree.right.cargo)*float(tree.left.right.cargo)
                tree.left = tree.left.left
            elif is_float(tree.left.left.cargo):
                tree.right.cargo = float(tree.right.cargo)*float(tree.left.left.cargo)
                tree.left = tree.left.right
    if tree.right != None: tree.right = simplify(tree.right)
    if tree.left != None: tree.left = simplify(tree.left)
    return tree

def orders(tree,test=False,first=False):                 # makes a list of the coefficients of increasing powers of x
    if tree == None: return
    
    if tree.cargo in ["+","="] and not test:
        if is_float(tree.left.cargo): ordered[0] += float(tree.left.cargo)
        elif is_float(tree.right.cargo): ordered[0] += float(tree.right.cargo)
    if is_float(tree.cargo) and first: ordered[0] += float(tree.cargo)
    
    if tree.right == None or tree.left == None: return
    if tree.cargo == "^":
        if is_float(tree.right.cargo): return int(tree.right.cargo)
        else: return int(tree.left.cargo)
    if is_float(tree.left.cargo) and orders(tree.right,True) != None:
        ordered[orders(tree.right)] += float(tree.left.cargo)
    if is_float(tree.right.cargo) and orders(tree.left,True) != None:
        ordered[orders(tree.left)] += float(tree.right.cargo)
    if tree.cargo == "*" and not test:
        if tree.left.cargo == "x": ordered[1] += float(tree.right.cargo)
        elif tree.right.cargo == "x": ordered[1] += float(tree.left.cargo)
    orders(tree.left)
    orders(tree.right)

def solve(orders):          # Solves the final equation which is in the form ax**3 + bx**2 + cx + d = 0.
    if orders[3] != 0:
        "solve cubic"
    elif orders[2] != 0:
        [c,b,a] = orders[:3]
        sol1 = (-b+(b**2 - 4*a*c)**0.5)/(2*a)
        sol2 = (-b-(b**2 - 4*a*c)**0.5)/(2*a)
        return [sol1,sol2]
    elif orders[1] != 0:
        return -orders[0]/orders[1]
    else:
        return orders[0]

def calculate(values):    # Uses suvat to calculate the missing value.
    print(values)
    equation = choose_equation(values)
    equation = add_numbers(equation,values)
    simplify(equation.left)
    simplify(equation.right)
    simplify(equation.left)
    simplify(equation.right)
    simplify(equation.left)
    simplify(equation.right)
    global ordered
    ordered = [0,0,0,0]
    orders(equation.left,first=True)
    ordered,left_orders = [0,0,0,0],ordered
    orders(equation.right,first=True)
    ordered,right_orders = [0,0,0,0,0],ordered
    total_orders = [0,0,0,0]
    for i in range(4):
        total_orders[i] += right_orders[i] - left_orders[i]
    print(solve(total_orders))

# SUVAT equations as trees
no_s = Tree("=",Tree("v"),Tree("+",Tree("u"),Tree("*",Tree("a"),Tree("t"))))                                                                           # v = u + a * t
no_u = Tree("=",Tree("s"),Tree("+", Tree("*",Tree("v"),Tree("t")), Tree("*",Tree("*",Tree(-0.5),Tree("a")),Tree("^",Tree("t"),Tree(2)))))              # s = vt - 0.5*at^2
no_v = Tree("=",Tree("s"),Tree("+", Tree("*",Tree("u"),Tree("t")), Tree("*",Tree("*",Tree(0.5),Tree("a")),Tree("^",Tree("t"),Tree(2)))))               # s = ut + 0.5*at^2
no_a = Tree("=",Tree("s"),Tree("*",Tree("*",Tree(0.5),Tree("t")),Tree("+",Tree("u"),Tree("v"))))                                                       # s = 0.5*(u+v)t
no_t = Tree("=",Tree("*",Tree("^",Tree("v"),Tree(2)),Tree(1)),Tree("+",Tree("^",Tree("u"),Tree(2)),Tree("*",Tree("*",Tree("a"),Tree("s")),Tree(2))))   # v^2 = u^2 + 2as

equations = {"s":no_s,"u":no_u,"v":no_v,"a":no_a,"t":no_t}


while True:
    print('''
This is the menu -------------------
1. Solve one question
2. Solve a lot of questions
3. Exit''')
    while True:
        try:
            choice = int(input("Enter a choice: "))
            if choice in [1,2,3]: break
            else: print("Invalid choice.")
        except: print("Invalid choice.")
    if choice == 1: calculate(input_values())
    elif choice == 2:
        inputs = input_bulk()
        for values in inputs:
            calculate(values)
    elif choice == 3: exit()


# This code is for debugging, it prints out working.
'''
while True:
    values = input_values()

    equation = choose_equation(values)
    print_tree(equation)
    print()
    equation = add_numbers(equation,values)
    print_tree(equation)
    print()
    print(contains_x(equation.left),contains_x(equation.right))

    simplify(equation.left)
    simplify(equation.right)
    print_tree(equation)
    print()
    simplify(equation.left)
    simplify(equation.right)
    print_tree(equation)
    print()
    simplify(equation.left)
    simplify(equation.right)
    print_tree(equation)
    print()

    global ordered
    ordered = [0,0,0,0]
    orders(equation.left,first=True)
    ordered,left_orders = [0,0,0,0],ordered
    orders(equation.right,first=True)
    ordered,right_orders = [0,0,0,0,0],ordered
    print(left_orders,right_orders)
    total_orders = [0,0,0,0]
    for i in range(4):
        total_orders[i] += right_orders[i] - left_orders[i]
    print(total_orders)
    print(solve(total_orders))
'''





