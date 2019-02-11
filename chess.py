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

    #check all and append all cells until met ally or enemy or outside of board
    def possible_moves(self, start_pos, target_pos):
        valid_moves = []
        #legal moves "to the right"
        for x in range(start_pos[1]+1, 8):
            if board.BOARD[start_pos[0]][x] != '.' and board.BOARD[start_pos[0]][x].team == 'W':
                break
            if board.BOARD[start_pos[0]][x] == '.':
                valid_moves.append([start_pos[0], x])
        
        #legal moves "to the left"
        for x in range(start_pos[1]-1, -1, -1):
            if board.BOARD[start_pos[0]][x] != '.' and board.BOARD[start_pos[0]][x].team == 'W':
                break
            if board.BOARD[start_pos[0]][x] == '.':
                valid_moves.append([start_pos[0], x])

        #legal moves "to the bottom"
        for x in range(start_pos[0]+1, 7):
            if board.BOARD[x][start_pos[1]] != '.' and board.BOARD[x][start_pos[1]].team == 'W':
                break
            if board.BOARD[x][start_pos[1]] == '.':
                valid_moves.append([x, start_pos[1]])

        #legal moves "to the top"
        for x in range(start_pos[0]-1, -1, -1):
            if board.BOARD[x][start_pos[1]] != '.' and board.BOARD[x][start_pos[1]].team == 'W':
                break
            if board.BOARD[x][start_pos[1]] == '.':
                valid_moves.append([x, start_pos[1]])

        return valid_moves
class Board:
    white_pieces = []
    def __init__(self):
        self.BOARD = [["."]*8 for i in range(8)]

    def place(self, pos, piece):
        self.BOARD[pos[0]][pos[1]] = piece
    
    def initWhites(self): #jedna funkcja dla obu druzyn?
        for i in range(8):
            self.white_pieces.append(Pawn([6, i], "W"))
        self.white_pieces.append(Rook([7, 0], "W"))
        self.white_pieces.append(Rook([7, 7], "W"))

    def valid_move(self, start_pos, target_pos):
        print(self.BOARD[start_pos[0]][start_pos[1]].possible_moves(start_pos, target_pos)) #czy nie za poza

 #   def move(self, start_pos, target_pos):
 #       if valid_move(start_pos, target_pos):

    def printBoard(self):
        for i in self.BOARD:
            for j in i:
                print(j, end="")
            print('')
    

board = Board()
board.initWhites()
board.printBoard()
board.valid_move([7,0], [7,1])
