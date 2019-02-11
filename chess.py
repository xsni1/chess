class Piece:
    def __init__(self, pos, team):
        self.pos = pos
        self.team = team
        board.place(pos, self)
        
    def __str__(self):
        return self.symbol

class Pawn(Piece):
    symbol = "P"
    def __init__(self, pos, team):
        super().__init__(pos, team)

class Rook(Piece):
    symbol = "R"
    def __init__(self, pos, team):
        super().__init__(pos, team)

class Board:
    white_pieces = []
    def __init__(self):
        self.BOARD = [["."]*8 for i in range(8)]

    def place(self, pos, piece):
        self.BOARD[pos[0]][pos[1]] = piece
    
    def initWhites(self):
        for i in range(8):
            self.white_pieces.append(Pawn([6, i], "W"))

    def printBoard(self):
        for i in self.BOARD:
            for j in i:
                print(j, end="")
            print('')
    

board = Board()
board.initWhites()
board.printBoard()
