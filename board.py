
class Board:
    """This class defines the Board for a game of Connect Four
    it also contains the functions needed to perform the moves
    and can determine a full Board, a win, or draw """

    maxX = 7
    maxY = 6

    emptySpace = 0
    playerMove = 1
    computerMove = 2

    def __init__(self):
        "Sets up a blank Board"
        self.spaces = [[Board.emptySpace for i in range(Board.maxY)] for j in range(Board.maxX)]

    def setSpace(self, x, y, val):
        "Sets an individual space"
        if x >= Board.maxX or y >= Board.maxY:
            raise IndexError

        if type(val) is not int:
            raise TypeError

        if val != Board.emptySpace and val != Board.playerMove and val != Board.computerMove:
            raise ValueError

        self.spaces[x][y] = val

    def getSpace(self, x, y):
        "Returns an individual space"
        if x >= Board.maxX or y >= Board.maxY:
            raise IndexError
        return self.spaces[x][y]


    def setBoard(self, newSpaces):
        """ Replaces the entire Board.  Check only if the first row is the right length
        does not check values.  Used as a setup shortcut for testing only. """
        if len(newSpaces[1]) != Board.maxY or len(newSpaces) != Board.maxX:
            raise ValueError
        else:
            self.spaces = newSpaces[:]

    def dropTile(self, x, tile):
        """Slides a tile down the selected row.  If the drop worked, a tuple of the
        landing square is returned, else None."""
        if tile != Board.emptySpace and tile != Board.playerMove and tile != Board.computerMove:
            raise ValueError

        if x < 0 or x >= Board.maxX:
            return None

        if tile != Board.emptySpace and tile != Board.playerMove and tile != Board.computerMove:
            raise ValueError

        if self.spaces[x][0] != Board.emptySpace:
            return None

        for y in range(Board.maxY-1):
            if self.spaces[x][y+1] != Board.emptySpace:
                self.setSpace(x,y,tile)
                return x,y

        if Board.emptySpace == self.spaces[x][Board.maxY-1]:
            self.setSpace(x,Board.maxY-1,tile)
            return x,Board.maxY-1

    def boardFull(self):
        for y in range(Board.maxY):
            for x in range(Board.maxX):
                if self.getSpace(x, y) == Board.emptySpace:
                    return False
        return True

    def hasForwardDiagonalWinner(self):
        pass

    def hasForwardDiagonalWinner(self):
        pass

    def hasVerticalWinner(self):
        pass

    def hasHorizontalWinner(self):
        pass

    def __str__(self):
        "Pretty print of the Board"
        print "  0 1 2 3 4 5 6"
        for y in range(Board.maxY):
            print y,
            for x in range(Board.maxX):
                print self.getSpace(x, y),
            print
        return str(self.spaces)

if __name__ == "__main__":
    myBoard = Board()

    myBoard.setSpace(5, 3, Board.playerMove)

    str(myBoard)
    
    