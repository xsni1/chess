class Piece:
    def __init__(self, pos, team):
        self.pos = pos
        self.team = team
        board.place(pos, self)
        
    def __str__(self):
        return self.symbol

class King(Piece):
    symbol = 'K'
    def __init__(self, pos, team):
        super().__init__(pos, team)
    def possible_moves(self, start_pos):
        return []

class Pawn(Piece):
    symbol = 'P'
    moved = False
    def __init__(self, pos, team):
        super().__init__(pos, team)
    def possible_moves(self, start_pos):
        if self.team == 'W':
            direction = -1
        else:
            direction = 1
        attacking_moves = [[start_pos[0] + direction, start_pos[1] - direction], [start_pos[0] + direction, start_pos[1] + direction]]
        attacking_moves = list(filter(lambda move: move[0]>=0 and move[0]<=7 and move[1] >= 0 and move[1] <= 7 and chessboard[move[0]][move[1]] != '.' and chessboard[move[0]][move[1]].team != chessboard[start_pos[0]][start_pos[1]].team, attacking_moves))
        if not self.moved:
            all_moves = [[start_pos[0] + direction, start_pos[1]], [start_pos[0] + 2*direction, start_pos[1]]]
        else:
            all_moves = [[start_pos[0] + direction, start_pos[1]]]
        self.attacking = False
        return [move for move in all_moves if move[0]>=0 and move[0] <= 7 and chessboard[move[0]][move[1]] == '.'] + attacking_moves if chessboard[start_pos[0] + direction][start_pos[1]] == '.' else [] #pawn can only move if there is no figure in front of it

class Knight(Piece):
    symbol = 'N'
    def __init__(self, pos, team):
        super().__init__(pos, team)
    
    def possible_moves(self, start_pos): 
        all_moves = [[start_pos[0]-2, start_pos[1]+1], [start_pos[0]-2, start_pos[1]-1], [start_pos[0]+2, start_pos[1]+1], [start_pos[0]+2, start_pos[1]-1]]
        return [move for move in all_moves if move[0]>=0 and move[0]<=7 and move[1]>=0 and move[1]<=7 and (chessboard[move[0]][move[1]] == '.' or chessboard[move[0]][move[1]].team == 'B')]

class Queen(Piece):
    symbol = 'Q'
    def __ini__(self, pos, team):
        super().__init__(pos, team)
    def possible_moves(self, start_pos):
        return Bishop.possible_moves(start_pos) + Rook.possible_moves(start_pos)

class Bishop(Piece):
    symbol = 'B'
    def __init__(self, pos, team):
        super().__init__(pos, team)
    @staticmethod
    def possible_moves(start_pos):
        valid_moves = []
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
    symbol = 'R'
    def __init__(self, pos, team):
        super().__init__(pos, team)

    #check all and append all cells until met ally or enemy or outside of board
    @staticmethod
    def possible_moves(start_pos):
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
        self.BOARD = [['.']*8 for i in range(8)]

    def place(self, pos, piece):
        self.BOARD[pos[0]][pos[1]] = piece
    
    def initWhites(self): #jedna funkcja dla obu druzyn?
        for i in range(8):
            self.white_pieces.append(Pawn([6, i], 'W'))
        self.white_pieces.append(Rook([7, 0], 'W'))
        self.white_pieces.append(Rook([7, 7], 'W'))
        self.white_pieces.append(Knight([7, 1], 'B'))
        self.white_pieces.append(Knight([7, 6], 'W'))
        self.white_pieces.append(Bishop([7, 2], 'W'))
        self.white_pieces.append(Bishop([7, 5], 'W'))
        self.white_pieces.append(Queen([7,3], 'W'))

    def valid_move(self, start_pos, target_pos):
        if target_pos in self.BOARD[start_pos[0]][start_pos[1]].possible_moves(start_pos): #czy nie za poza
            return True

    def move(self, start_pos, target_pos):
        if self.valid_move(start_pos, target_pos):
            if self.BOARD[start_pos[0]][start_pos[1]].symbol == 'P':
                self.BOARD[start_pos[0]][start_pos[1]].moved = True
            self.BOARD[start_pos[0]][start_pos[1]].pos = [[target_pos[0]], [target_pos[1]]]
            self.BOARD[target_pos[0]][target_pos[1]] = self.BOARD[start_pos[0]][start_pos[1]]  #jak mozna unzipowac zamiast target_pos[0] i [1]
            self.BOARD[start_pos[0]][start_pos[1]] = '.'
        else:
            print('Move not legal')

    def printBoard(self):
        ind = 8
        for i in self.BOARD:
            for j in i:
                print(str(j) + ' ', end="")
            print(' ' + str(ind))
            ind -= 1
        print('')
        for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            print(i + ' ', end='')
    

board = Board()
chessboard = board.BOARD
board.initWhites()
while True:
    board.printBoard()
    print('\nyour move:')
    move = input() # "a3d4" a3 current location d4 target location
    current_pos = [7-int(move[1])+1, ord(move[0])-97]
    target_pos = [7-int(move[3])+1, ord(move[2])-97]
    board.move(current_pos, target_pos)