from pieces import *

class Board:

    def __init__(self):
        self.board = {}
        self.placePieces()

    def placePieces(self):
        self.board = {}
        self.board = {   "B1": ("Black", "Pawn"), "B2": ("Black", "Pawn"), "B3": ("Black", "Pawn"), "B4": ("Black", "Pawn"),
                         "B5": ("Black", "Pawn"), "B6": ("Black", "Pawn"), "B7": ("Black", "Pawn"), "B8": ("Black", "Pawn"),
                         "A1": ("Black", "Rook"), "A8": ("Black", "Rook"), "A2": ("Black", "Knight"), "A7": ("Black", "Knight"),
                         "A3": ("Black", "Bishop"), "A6": ("Black", "Bishop"), "A5": ("Black", "King"), "A4": ("Black", "Queen"),
                         "G1": ("White", "Pawn"), "G2": ("White", "Pawn"), "G3": ("White", "Pawn"), "G4": ("White", "Pawn"),
                         "G5": ("White", "Pawn"), "G6": ("White", "Pawn"), "G7": ("White", "Pawn"), "G8": ("White", "Pawn"),
                         "H1": ("White", "Rook"), "H8": ("White", "Rook"), "H2": ("White", "Knight"), "H7": ("White", "Knight"),
                         "H3": ("White", "Bishop"), "H6": ("White", "Bishop"), "H4": ("White", "Queen"), "H5": ("White","King")}

    def setPiece(self, position, piece):
        letter = str(position[0])
        number = str(position[1])
        pos = letter + number
        self.board[pos] = (piece[0], piece[1])

    def getPiece(self, position):
        letter = str(position[0])
        number = str(position[1])
        pos = letter + number
        if self.board[pos][1] == "Pawn":
            return Pawn(self.board[pos][0], self, position)
        elif self.board[pos][1] == "Knight":
            return Knight(self.board[pos][0], self, position)
        elif self.board[pos][1] == "Bishop":
            return Bishop(self.board[pos][0], self, position)
        elif self.board[pos][1] == "Queen":
            return Queen(self.board[pos][0], self, position)
        elif self.board[pos][1] == "King":
            return King(self.board[pos][0], self, position)
        elif self.board[pos][1] == "Rook":
            return Rook(self.board[pos][0], self, position)
        return None

    def makeMove(self, startPosition, endPosition, player):
        letter = str(startPosition[0])
        number = str(startPosition[1])
        pos = letter + number
        if self.getPiece(startPosition) != None:
            if player == "Black":
                self.setPiece(endPosition, self.board[pos])
                self.board.pop(pos)
            if player == "White":
                self.setPiece(endPosition, self.board[pos])
                self.board.pop(pos)
        else:
            print("The piece doesn't exist, move can't be made")


    def displayBoard(self):
        board_lst = []
        for i in range(65, 73):
            row_list = []
            for j in range(1, 9):
                self_pos = str(chr(i) + str(j))
                if self_pos in self.board.keys():
                    color = self.board[self_pos][0]
                    piece = self.board[self_pos][1]
                    if color == "White":
                        row_list.append("[{}]".format(whiteIcons[piece]))
                    else:
                        row_list.append("[{}]".format(blackIcons[piece]))
                else:
                    row_list.append("[ ]")
            board_lst.append(row_list)

        print("   ", end="")
        for i in range(1, 9):
            print("({})".format(i), end="")
        print()
        for i in range(65, 73):
            print("({})".format(chr(i)), end="")
            for j in range(1, 9):
                print(board_lst[i - 65][j - 1], end="")
            print()
        print()

