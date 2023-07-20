blackIcons = {"Pawn": "♙", "Rook": "♖", "Knight": "♘", "Bishop": "♗", "King": "♔", "Queen": "♕"}
whiteIcons = {"Pawn": "♟", "Rook": "♜", "Knight": "♞", "Bishop": "♝", "King": "♚", "Queen": "♛"}


class Piece:

    def __init__(self, color, board, position):
        self.__color = color
        self._board = board
        self.__position = position

    def position_valid(self, new_position):
        if len(new_position) == 2 and ord(new_position[0]) >= 65 and ord(new_position[0]) <= 72 \
                and int(new_position[1]) >= 1 and int(new_position[1]) <= 8:
            return True
        return False

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        if self.position_valid(new_position):
            self.__position = new_position
        else:
            raise ValueError("Invalid position")

    def checkMove(self, dest):
        if not self.position_valid(dest) or dest == self.position:
            return False
        return True

    def move(self, dest):
        return False

    def getName(self):
        return "piece"

    def getIcon(self):
        return None


class Knight(Piece):
    def checkMove(self, dest):
        if not super().checkMove(dest):
            return False
        letter = str(dest[0])
        number = str(dest[1])
        des = letter + number
        for key in self._board.board:
            if (key == des and self._board.board[des][0] == self.color) or (key == des and self._board.board[des][1] == "King"):
                return False

        dx = abs(ord(dest[0]) - ord(self.position[0]))
        dy = abs(dest[1] - self.position[1])

        return (dx, dy) in [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]

    def move(self, dest):
        letter = str(dest[0])
        number = str(dest[1])
        des = letter + number
        letter2 = str(self.position[0])
        number2 = str(self.position[1])
        pos = letter2 + number2
        if self.checkMove():
            self.position = dest
            self._board.board[des] = self._board.board[pos]
            self._board.board.pop(pos)

    def getName(self):
        return "Knight"

    def getIcon(self):
        return whiteIcons["Knight"] if self.color == "White" else blackIcons["Knight"]


class Rook(Piece):
    def checkMove(self, dest):
        if not super().checkMove(dest) and (dest[0] != self.position[0] and dest[1] != self.position[1]):
            return False
        letter = str(dest[0])
        number = str(dest[1])
        des = letter + number
        for key in self._board.board:
            if (key == des and self._board.board[des][0] == self.color) or (
                    key == des and self._board.board[des][1] == "King"):
                return False

        if self.color == "White":
            start = ord(self.position[0]) - 1
            end = ord(dest[0]) + 1
            step = 1 if start < end else -1
            for x in range(start, end, step):
                if str(chr(x)) + str(des[1]) in self._board.board:
                    return False
        else:
            start = self.position[1] + 1
            end = dest[1] - 1
            step = 1 if start < end else -1
            for y in range(start, end, step):
                if str(dest[0]) + str(y) in self._board.board:
                    return False
        return True

    def move(self, dest):
        letter = str(dest[0])
        number = str(dest[1])
        des = letter + number
        letter2 = str(self.position[0])
        number2 = str(self.position[1])
        pos = letter2 + number2
        if self.checkMove():
            self.position = dest
            self._board.board[des] = self._board.board[pos]
            self._board.board.pop(pos)

    def getName(self):
        return "Rook"

    def getIcon(self):
        return whiteIcons["Rook"] if self.color == "White" else blackIcons["Rook"]


class Bishop(Piece):
    def checkMove(self, dest):
        if not super().checkMove(dest) and (abs(ord(dest[0]) - ord(self.position[0])) != abs(dest[1] - self.position[1])):
            return False

        letter = str(dest[0])
        number = str(dest[1])
        des = letter + number
        for key in self._board.board:
            if (key == des and self._board.board[des][0] == self.color) or (
                    key == des and self._board.board[des][1] == "King"):
                return False

        dx = 1 if ord(dest[0]) - 64 > ord(self.position[0]) - 64 else -1
        dy = 1 if dest[1] > self.position[1] else -1
        x = ord(self.position[0]) - 64 + dx
        y = self.position[1] + dy

        while x != ord(dest[0]) - 64 and y != dest[1]:
            let = str(chr(x + 64))
            num = str(y)
            pos = let + num
            for key in self._board.board:
                if key == pos:
                    return False
            x += dx
            y += dy
        return True

    def move(self, dest):
        letter = str(dest[0])
        number = str(dest[1])
        des = letter + number
        letter2 = str(self.position[0])
        number2 = str(self.position[1])
        pos = letter2 + number2
        if self.checkMove():
            self.position = dest
            self._board.board[des] = self._board.board[pos]
            self._board.board.pop(pos)

    def getName(self):
        return "Bishop"

    def getIcon(self):
        return whiteIcons["Bishop"] if self.color == "White" else blackIcons["Bishop"]


class Queen(Piece):
    def checkMove(self, dest):
        if not super().checkMove(dest):
            return False

        dx = abs(ord(dest[0]) - ord(self.position[0]))
        dy = abs(dest[1] - self.position[1])


        letter = str(dest[0])
        number = str(dest[1])
        des = letter + number
        for key in self._board.board:
            if (key == des and self._board.board[des][0] == self.color) or (
                    key == des and self._board.board[des][1] == "King"):
                return False

        if dx == 0 or dy == 0 or dx == dy:
            if abs((ord(dest[0])) - ord(self.position[0]) == abs(dest[1] - self.position[1])):
                x_dir = 1 if ord(dest[0]) > ord(self.position[0]) else -1
                y_dir = 1 if dest[1] > self.position[1] else -1
                x = ord(self.position[0]) - 64 + x_dir
                y = self.position[1] + y_dir

                while x != ord(dest[0]) - 64 and y != dest[1]:
                    let = str(chr(x + 64))
                    num = str(y)
                    pos = let + num
                    for key in self._board.board:
                        if key == pos:
                            return False
                    x += x_dir
                    y += y_dir
            else:
                if dest[0] != self.position[0]:
                    start = ord(self.position[0]) - 63
                    end = ord(dest[0]) - 65
                    step = 1 if start < end else -1
                    for x in range(start, end, step):
                        if str(chr(x + 64)) + str(des[1]) in self._board.board:
                            return False
                else:
                    start = self.position[1] + 1
                    end = dest[1] - 1
                    step = 1 if start < end else -1
                    for y in range(start, end, step):
                        if str(dest[0]) + str(y) in self._board.board:
                            return False
        else:
            return False
        
        return True

    def move(self, dest):
        letter = str(dest[0])
        number = str(dest[1])
        des = letter + number
        letter2 = str(self.position[0])
        number2 = str(self.position[1])
        pos = letter2 + number2
        if self.checkMove():
            self.position = dest
            self._board.board[des] = self._board.board[pos]
            self._board.board.pop(pos)

    def getName(self):
        return "Queen"

    def getIcon(self):
        return whiteIcons["Queen"] if self.color == "White" else blackIcons["Queen"]


class King(Piece):
    def checkMove(self, dest):
        if not super().checkMove(dest):
            return False

        letter = str(dest[0])
        number = str(dest[1])
        des = letter + number
        for key in self._board.board:
            if key == des and self._board.board[des][0] == self.color:
                return False

        dx = abs(ord(dest[0]) - ord(self.position[0]))
        dy = abs(dest[1] - self.position[1])

        return dx <= 1 and dy <= 1

    def move(self, dest):
        letter = str(dest[0])
        number = str(dest[1])
        des = letter + number
        letter2 = str(self.position[0])
        number2 = str(self.position[1])
        pos = letter2 + number2
        if self.checkMove():
            self.position = dest
            self._board.board[des] = self._board.board[pos]
            self._board.board.pop(pos)

    def getName(self):
        return "King"

    def getIcon(self):
        return whiteIcons["King"] if self.color == "White" else blackIcons["King"]


class Pawn(Piece):
    def checkMove(self, dest):
        if not super().checkMove(dest):
            return False

        dx = (ord(dest[0]) - ord(self.position[0]))
        dy = (dest[1] - self.position[1])

        letter = str(dest[0])
        number = str(dest[1])
        des = letter + number
        for key in self._board.board:
            if self.color == "White" and (key == des and self._board.board[des][0] != self.color) and \
                    (key == des and self._board.board[des][1] != "King") and ((dy == 1 and dx == -1) or (dy == -1 and dx == -1)):
                return True
            elif self.color == "Black" and (key == des and self._board.board[des][0] != self.color) and \
                (key == des and self._board.board[des][1] != "King") and ((dy == 1 and dx == 1) or (dy == -1 and dx == 1)):
                return True
            
        if self.color == "White" and (dy == 0 and dx == -1):
            return True
        elif self.color == "Black" and (dy == 0 and dx == 1):
            return True
        if self.color == "White" and self.position[0] == 'G' and dx == -2 and dy == 0:
            return True
        elif self.color == "Black" and self.position[0] == 'B' and dx == 2 and dy == 0:
            return True

        return False

    def move(self, dest):
        letter = str(dest[0])
        number = str(dest[1])
        des = letter + number
        letter2 = str(self.position[0])
        number2 = str(self.position[1])
        pos = letter2 + number2
        if self.checkMove():
            self.position = dest
            self._board.board[des] = self._board.board[pos]
            self._board.board.pop(pos)

    def getName(self):
        return "Pawn"

    def getIcon(self):
        return whiteIcons["Pawn"] if self.color == "White" else blackIcons["Pawn"]