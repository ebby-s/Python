class board:

    def __init__(self):
        '''A chess board'''
        self.convert = {0:"empty",1:"pawn",2:"castle",3:"knight",4:"bishop",5:"queen",6:"king"}
        self.cols = [[] for x in range(8)]
        for i in range(8):
            self.cols[i] = [piece(0) for x in range(8)]

        for i,col in enumerate(self.cols):
            col[1] = piece(1)
            col[-2] = piece(-1)
            if i in [0,7]:
                col[0] = piece(2)
                col[-1] = piece(-2)
            elif i in [1,6]:
                col[0] = piece(3)
                col[-1] = piece(-3)
            elif i in [2,5]:
                col[0] = piece(4)
                col[-1] = piece(-4)
            elif i == 3:
                col[0] = piece(5)
                col[-1] = piece(-5)
            elif i == 4:
                col[0] = piece(6)
                col[-1] = piece(-6)

    def show_board(self):
        rows = [[] for x in range(8)]
        for col in self.cols:
            for j,piece in enumerate(col):
                if piece.type >= 0:
                    rows[j].append(" "+str(piece.type))
                else:
                    rows[j].append(str(piece.type))
        for row in rows:
            print(row)

    def move_piece(self,c_piece,target):
        if c_piece[0] not in range(8) or c_piece[1] not in range(8):
            return 'piece not on board'
        elif target[0] not in range(8) or target[1] not in range(8):
            return 'target not on board'
        elif c_piece == target:
            return "piece is already on target"
        elif self.cols[c_piece[0]][c_piece[1]].type == 0:
            return 'empty box'
        elif self.cols[target[0]][target[1]]*self.cols[c_piece[0]][c_piece[1]] > 0:
            return 'target is not empty'

        if self.cols[c_piece[0]][c_piece[1]].move(c_piece,target):
            self.cols[target[0]][target[1]] = self.cols[c_piece[0]][c_piece[1]]
            self.cols[c_piece[0]][c_piece[1]] = piece(0)
        else:
            return 'invalid move'

class piece:

    def __init__(self,name):
        '''A chess piece'''
        self.type = name

    def repr(self):
        return str(self.type)

    def __mul__(self,other):
        return self.type*other.type

    def move(self,current,target):
        movement = [target[0]-current[0],target[1]-current[1]]
        if abs(self.type) == 1:
            print("pawn")
            if current[1] in [1,6]:
                print("pawn first")
                if current[0] == target[0] and self.type*(target[1] - current[1]) in [1,2]:
                    return True
            else:
                if current[0] == target[0] and self.type*(target[1] - current[1]) == 1:
                    return True
        if abs(self.type) == 2:
            if current[0] == target[0] or current[1] == target[1]:
                return True
        if abs(self.type) == 3 and movement[0] != 0:
            if abs(movement[1]/movement[0]) == 1:
                return True
        if abs(self.type) == 4:
            "idk rn lol"
        if abs(self.type) == 5:
            if current[0] == target[0] or current[1] == target[1] or movement[1]/movement[0] == 1:
                return True
        if abs(self.type) == 6:
            "later"
        return False 

test_board = board()
while True:
    test_board.show_board()
    while True:
        try:
            c_piece = [int(x) for x in input("Piece to move: ").split()]
            target = [int(x) for x in input("Target location: ").split()]
            if len(c_piece) == 2 and len(target) == 2:
                break
            else:
                print("Invalid input")
        except:
            print("Invalid input")
    print(test_board.move_piece(c_piece,target))
