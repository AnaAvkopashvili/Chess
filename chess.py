from board import Board
from pieces import *

class Chess:
    def __init__(self):
        self.board = Board()
        self.currentPlayer = "White"

    def swapPlayers(self):
        if self.currentPlayer == "White":
            self.currentPlayer = "Black"
        else:
            self.currentPlayer = "White"

    def isStringValidMove(self, moveStr):
        if len(moveStr) == 5 and 65 <= ord(moveStr[0]) <= 72 and 1 <= int(moveStr[1]) <= 8 and moveStr[2] == " " and 65 <= ord(moveStr[3]) <= 72 and 1 <= int(moveStr[4]) <= 8:
            return True
        return False

    def checkPromotion(self, piece, endPosition):
        if isinstance(piece, Pawn):
            if endPosition[0] == 'A' or endPosition[0] == 'H':
                return True
        return False

    def promotePawn(self, piece, endPosition):
            promotedPiece = None
            while promotedPiece not in ["Q", "R", "B", "N"]:
                promotedPiece = input("Choose a piece to promote the pawn (Q/R/B/N): ")
            if promotedPiece == "Q":
                self.board.setPiece(endPosition, (self.currentPlayer, "Queen"))
            elif promotedPiece == "R":
                self.board.setPiece(endPosition, (self.currentPlayer, "Rook"))
            elif promotedPiece == "B":
                self.board.setPiece(endPosition, (self.currentPlayer, "Bishop"))
            elif promotedPiece == "N":
                self.board.setPiece(endPosition, (self.currentPlayer, "Knight"))


    def play(self):
        self.board.displayBoard()
        print("White's turn. Enter a move: ")
        while(True):
            while (True):
                inp = input()
                if inp == "EXIT":
                    return
                elif not self.isStringValidMove(inp):
                    print("Invalid move, please try again:")
                    continue

                start = (inp[0], int(inp[1]))
                end = (inp[3], int(inp[4]))
                start_str = str(inp[0]) + str(inp[1])
                if (start_str not in self.board.board.keys()) or (self.board.board[start_str][0] != self.currentPlayer):
                    print("No right piece found in the start position, please try again: ")
                    continue
                piece = self.board.getPiece(start)
                if not piece.checkMove(end):
                    print("You cant make this move, please try again: ")
                    continue
                break
            start = (inp[0], int(inp[1]))
            end = (inp[3], int(inp[4]))
            piece = self.board.getPiece(start)
            self.board.makeMove((inp[0], int(inp[1])), (inp[3], int(inp[4])), self.currentPlayer)
            if self.checkPromotion(piece, (inp[3], int(inp[4]))):
                self.promotePawn(piece, (inp[3], int(inp[4])))
            self.swapPlayers()
            self.board.displayBoard()
            print(f"{self.currentPlayer}'s turn. Enter a move: ")

if __name__ == "__main__":
    game = Chess()
    game.play()