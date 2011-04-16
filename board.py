class BoardBase:
    emptySpace = 0
    playerMove = 1
    computerMove = 2

    def __init__(self):
        pass

    def getSpace(self, x, y):
        "Return the contents of a given space on a board"
        return None

    def setSpace(self, x, y):
        "Set the space on a board"
        pass

    def makeMove(self, x, tile):
        "Allow a player to move"
        return None

    def hasWinner(self):
        "Check to see if someone has won.  Return None if no one has won"
        pass


class ConnectFourBoard(BoardBase):
    """This class defines the ConnectFourBoard for a game of Connect Four
    it also contains the functions needed to perform the moves
    and can determine a full ConnectFourBoard, a win, or draw """

    maxX = 7
    maxY = 6

    def __init__(self):
        "Sets up a blank ConnectFourBoard"
        self.spaces = [[ConnectFourBoard.emptySpace for i in range(ConnectFourBoard.maxY)] for j in
                       range(ConnectFourBoard.maxX)]

    def setSpace(self, x, y, val):
        "Sets an individual space"
        if x >= ConnectFourBoard.maxX or y >= ConnectFourBoard.maxY:
            raise IndexError

        if type(val) is not int:
            raise TypeError

        if val != ConnectFourBoard.emptySpace and val != ConnectFourBoard.playerMove and val != ConnectFourBoard.computerMove:
            raise ValueError

        self.spaces[x][y] = val

    def getSpace(self, x, y):
        "Returns an individual space"
        if x >= ConnectFourBoard.maxX or y >= ConnectFourBoard.maxY or x < 0 or y < 0:
            return None
        return self.spaces[x][y]


    def setBoard(self, newSpaces):
        """ Replaces the entire ConnectFourBoard.  Check only if the first row is the right length
        does not check values.  Used as a setup shortcut for testing only. """
        if len(newSpaces[1]) != ConnectFourBoard.maxY or len(newSpaces) != ConnectFourBoard.maxX:
            raise ValueError
        else:
            self.spaces = newSpaces[:]

    def makeMove(self, x, tile):
        """Slides a tile down the selected row.  If the drop worked, a tuple of the
        landing square is returned, else None."""
        if tile != ConnectFourBoard.emptySpace and tile != ConnectFourBoard.playerMove and tile != ConnectFourBoard.computerMove:
            raise ValueError

        if x < 0 or x >= ConnectFourBoard.maxX:
            return None

        if tile != ConnectFourBoard.emptySpace and tile != ConnectFourBoard.playerMove and tile != ConnectFourBoard.computerMove:
            raise ValueError

        if self.spaces[x][0] != ConnectFourBoard.emptySpace:
            return None

        for y in range(ConnectFourBoard.maxY - 1):
            if self.spaces[x][y + 1] != ConnectFourBoard.emptySpace:
                self.setSpace(x, y, tile)
                return x, y

        if ConnectFourBoard.emptySpace == self.spaces[x][ConnectFourBoard.maxY - 1]:
            self.setSpace(x, ConnectFourBoard.maxY - 1, tile)
            return x, ConnectFourBoard.maxY - 1

    def boardFull(self):
        for y in range(ConnectFourBoard.maxY):
            for x in range(ConnectFourBoard.maxX):
                if self.getSpace(x, y) == ConnectFourBoard.emptySpace:
                    return False
        return True

    def hasDownwardDiagonalWinner(self, x, y):
        if x + 3 >= ConnectFourBoard.maxX or y + 3 >= ConnectFourBoard.maxY:
            return False
        else:
            return self.getSpace(x, y) == self.getSpace(x + 1, y + 1)\
                   and self.getSpace(x, y) == self.getSpace(x + 2, y + 2)\
            and self.getSpace(x, y) == self.getSpace(x + 3, y + 3)

    def hasUpwardDiagonalWinner(self, x, y):
        if x + 3 >= ConnectFourBoard.maxX or y - 3 < 0:
            return False
        else:
            return self.getSpace(x, y) == self.getSpace(x + 1, y - 1)\
                   and self.getSpace(x, y) == self.getSpace(x + 2, y - 2)\
            and self.getSpace(x, y) == self.getSpace(x + 3, y - 3)

    def hasVerticalWinner(self, x, y):
        if y + 3 >= ConnectFourBoard.maxY:
            return False
        else:
            return self.getSpace(x, y) == self.getSpace(x, y + 1)\
                   and self.getSpace(x, y) == self.getSpace(x, y + 2)\
            and self.getSpace(x, y) == self.getSpace(x, y + 3)

    def hasHorizontalWinner(self, x, y):
        if x + 3 >= ConnectFourBoard.maxX:
            return False
        else:
            return self.getSpace(x, y) == self.getSpace(x + 1, y)\
                   and self.getSpace(x, y) == self.getSpace(x + 2, y)\
            and self.getSpace(x, y) == self.getSpace(x + 3, y)

    def hasWinner(self):
        for y in range(ConnectFourBoard.maxY):
            for x in range(ConnectFourBoard.maxX):
                if self.spaces[x][y] != ConnectFourBoard.emptySpace:
                    if self.getSpace(x, y) == self.getSpace(x, y + 1):
                        if self.hasVerticalWinner(x, y):
                            return self.getSpace(x, y)
                    if self.getSpace(x, y) == self.getSpace(x + 1, y):
                        if self.hasHorizontalWinner(x, y):
                            return self.getSpace(x, y)
                    if self.getSpace(x, y) == self.getSpace(x + 1, y + 1):
                        if self.hasDownwardDiagonalWinner(x, y):
                            return self.getSpace(x, y)
                    if self.getSpace(x, y) == self.getSpace(x + 1, y - 1) and self.hasUpwardDiagonalWinner(x, y):
                        return self.getSpace(x, y)
        return None

    def prettyPrint(self):
        "Pretty print of the ConnectFourBoard"
        print "columns  1 2 3 4 5 6 7"
        for y in range(ConnectFourBoard.maxY):
            print "        ",
            for x in range(ConnectFourBoard.maxX):
                print self.getSpace(x, y),
            print
        return str(self.spaces)

    def __str__(self):
        return str(self.spaces)

if __name__ == "__main__":
    myBoard = ConnectFourBoard()

    myBoard.setSpace(5, 3, ConnectFourBoard.playerMove)

    str(myBoard)
    
    