class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def print_tree(tree):
    if tree is None: return
    print_tree(tree.left)
    print(tree.cargo, end=" ")
    print_tree(tree.right)

def substitute(tree,value):
    if tree.right != None:
        tree = substitute(tree.right,value)
    elif tree.left != None:
        tree= substitute(tree.left,value)
    if tree.cargo == value[0]:
        tree.cargo = value[1]
    return tree

def solve(equation,values):
    for key in values.keys():
        equation = substitute(equation,[key,values[key]])
    return equation

equation = Tree("=",Tree("s"),Tree("+", Tree(Tree("t"),Tree("u")), Tree("*",Tree("*",Tree(0.5),Tree("a")),Tree("**",Tree("t"),Tree(2)))))
values = {"u":2,"v":7,"a":5,"t":1}


print_tree(equation)
tree = solve(equation,values)
print_tree(equation)
