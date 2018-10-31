class board:

    def __init__(self):
        self.contents = [[" "," "," "] for i in range(3)]

    def turn(self,mark,pos):
        x = {"1":0,"2":1,"3":2}
        y = {"a":0,"b":1,"c":2}
        self.contents[y[pos[0]]][x[pos[1]]] = mark

    def show_board(self):
        for row in self.contents:
            print(row)

    def reset(self):
        self.contents = [[" "," "," "] for i in range(3)]

test = board()
while True:
    test.reset()
    for i in range(9):
        if i%2 == 0:
            mark = "o"
        else:
            mark = "x"
        pos = [x for x in input("Location: ").split()]
        test.turn(mark,pos)
        test.show_board()
