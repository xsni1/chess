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

class Knight(Piece):
    symbol = "K"
    def __init__(self, pos, team):
        super().__init__(pos, team)
    
    def possible_moves(self, start_pos): #sprawdzic czy pola nie sa zajete przez sojusznikow
        return [[start_pos[0]-2, start_pos[1]+1], [start_pos[0]-2, start_pos[1]-1], [start_pos[0]+2, start_pos[1]+1], [start_pos[0]+2, start_pos[1]-1]]        

class Bishop(Piece):
    symbol = "B"
    def __init__(self, pos, team):
        super().__init__(pos, team)
    
    def possible_moves(self, start_pos):
        valid_moves = []
        chessboard = board.BOARD
        x = start_pos[1]
        y = start_pos[0]
        #legal moves to the diagonal top right
        for i in range(1, 8):
            if y-i < 0 or x+i > 7 or (chessboard[y-i][x+i] != '.' and chessboard[y-i][x+i].team == 'W'):
                break
            if chessboard[y-i][x+i] == '.' or chessboard[y-i][x+i].team == 'B':
                valid_moves.append([y-i, x+i])
        #legal moves to the diagonal top left
        for i in range(1, 8):
            if y-i < 0 or x-i < 0 or (chessboard[y-i][x-i] != '.' and chessboard[y-i][x-i].team == 'W'):
                break
            if chessboard[y-i][x-i] == '.' or chessboard[y-i][x-i].team == 'B':
                valid_moves.append([y-i, x-i])
        #legal moves to the diagonal bottom left
        for i in range(1, 8):
            if y+i > 7 or x-i < 0 or (chessboard[y+i][x-i] != '.' and chessboard[y+i][x-i].team == 'W'):
                break
            if chessboard[y+i][x-i] == '.' or chessboard[y+i][x-i].team == 'B':
                valid_moves.append([y+i, x-i])
        #legal moves to the diagonal bottom right
        for i in range(1, 8):
            if y+i > 7 or x+i > 7 or (chessboard[y+i][x+i] != '.' and chessboard[y+i][x+i].team == 'W'):
                break
            if chessboard[y+i][x+i] == '.' or chessboard[y+i][x+i].team == 'B':
                valid_moves.append([y+i, x+i])
        return valid_moves

class Rook(Piece):
    symbol = "R"
    def __init__(self, pos, team):
        super().__init__(pos, team)

    #check all and append all cells until met ally or enemy or outside of board
    def possible_moves(self, start_pos):
        #zmienic teamy ze statycznych na zalezne od parametru
        valid_moves = []
        #legal moves "to the right"
        for x in range(start_pos[1]+1, 8):
            if board.BOARD[start_pos[0]][x] != '.' and board.BOARD[start_pos[0]][x].team == 'W':
                break
            if board.BOARD[start_pos[0]][x] == '.' or board.BOARD[start_pos[0]][x].team == 'B':
                valid_moves.append([start_pos[0], x])
        
        #legal moves "to the left"
        for x in range(start_pos[1]-1, -1, -1):
            if board.BOARD[start_pos[0]][x] != '.' and board.BOARD[start_pos[0]][x].team == 'W':
                break
            if board.BOARD[start_pos[0]][x] == '.':
                valid_moves.append([start_pos[0], x])

        #legal moves "to the bottom"
        for x in range(start_pos[0]+1, 8):
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
        self.white_pieces.append(Knight([7, 1], "W"))
        self.white_pieces.append(Knight([7, 6], "W"))
        self.white_pieces.append(Bishop([7, 2], 'W'))
        self.white_pieces.append(Bishop([7, 5], 'W'))

    def valid_move(self, start_pos, target_pos):
        if target_pos in self.BOARD[start_pos[0]][start_pos[1]].possible_moves(start_pos): #czy nie za poza
            return True

    def move(self, start_pos, target_pos):
        if self.valid_move(start_pos, target_pos):
            self.BOARD[target_pos[0]][target_pos[1]] = self.BOARD[start_pos[0]][start_pos[1]]  #jak mozna unzipowac zamiast target_pos[0] i [1]
            self.BOARD[start_pos[0]][start_pos[1]] = '.'
        else:
            print('Move not legal')

    def printBoard(self):
        for i in self.BOARD:
            for j in i:
                print(j, end="")
            print('')
    

board = Board()
board.initWhites()
board.printBoard()
move = input() # "a3d4" a3 current location d4 target location
current_pos = [7-int(move[1])+1, ord(move[0])-97]
target_pos = [7-int(move[3])+1, ord(move[2])-97]
board.printBoard()