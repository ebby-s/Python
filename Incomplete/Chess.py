class board:

    def __init__(self):
        '''A chess board'''
        self.convert = {0:"empty",1:"pawn",2:"castle",3:"knight",4:"bishop",5:"queen",6:"king"}
        self.cols = [[] for x in range(8)]                    # Makes chess board array
        for i in range(8):
            self.cols[i] = [piece(0) for x in range(8)]

        for i,col in enumerate(self.cols):  # Fills array with pieces
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

    def show_board(self):                   # Prints out the board
        rows = [[] for x in range(8)]
        for col in self.cols:
            for j,piece in enumerate(col):
                if piece.type >= 0:
                    rows[j].append(" "+str(piece.type))
                else:
                    rows[j].append(str(piece.type))
        for row in rows:
            print(row)

    def move_piece(self,c_piece,target):                                    # Checks if the move is possible and checks if piece.move() is true
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

        if self.cols[c_piece[0]][c_piece[1]].move(c_piece,target,self.cols):
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

    def move(self,current,target,board):                              # Checks if the move obeys the rules
        movement = [target[0]-current[0],target[1]-current[1]]
        if abs(self.type) in [3,6] and not self.clear_path(current,movement,board):
            return False
        
        if abs(self.type) == 1:
            if self.type*movement[1] > 0 and abs(movement[0]) == 1 and abs(movement[1]) == 1 and board[target[0]][target[1]].type*self.type < 0:
                return True
            elif current[1] in [1,6]:
                if movement[0] == 0 and self.type*movement[1] in [1,2]:
                    return True
            else:
                if movement[0] == 0 and self.type*movement[1] == 1:
                    return True
        if abs(self.type) == 2:
            if movement[0] == 0 or movement[1] == 0:
                return True
        if abs(self.type) == 3:
            if (abs(movement[0]) == 2 and abs(movement[1]) == 3) or (abs(movement[0]) == 3 and abs(movement[1]) == 2):
                return True
        if abs(self.type) == 4 and movement[0] != 0:
            if abs(movement[1]/movement[0]) == 1:
                return True
        if abs(self.type) == 5:
            if movement[0] == 0 or movement[1] == 0 or movement[1]/movement[0] == 1:
                return True
        if abs(self.type) == 6:
            if movement[0] in [-1,0,1] and movement[1] in [-1,0,1]:
                return True
        return False 

    def clear_path(self,location,movement,board): # Checks if there is a clear path for the chess piece to move
        if movement[0] == 0:
            for y in range(movement[1]):
                if board[location[0],location[1]+1+y].type*self.type == 1:
                    return False
        elif movement[1] == 0:
            for x in range(movement[0]):
                if board[location[0]+1+x,location[1]].type*self.type == 1:
                    return False
        
        return True

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
