"""Boards for games.  Each game should have all the operations
 needed to make a move, check a space, etc.  The idea is that
 the board base class contains the needed operations for almost
 any board game (Connect Four, Tic Tac Toe, Checkers, etc.)"""

class BoardBase:
    """ Basic moves for all board games. """
    
    EMPTY_SPACE = 0
    PLAYER_MOVE = 1
    COMPUTER_MOVE = 2

    def __init__(self):
        pass

    def get_space(self, x, y):
        "Return the contents of a given space on a board"
        return None

    def set_space(self, x, y, val):
        "Set the space on a board"
        pass

    def make_move(self, x, tile):
        "Allow a player to move"
        return None

    def has_winner(self):
        "Check to see if someone has won.  Return None if no one has won"
        pass


class ConnectFourBoard(BoardBase):
    """This class defines the ConnectFourBoard for a game of Connect Four
    it also contains the functions needed to perform the moves
    and can determine a full ConnectFourBoard, a win, or draw """

    MAX_X = 7
    MAX_Y = 6

    def __init__(self):
        "Sets up a blank ConnectFourBoard"
        self.spaces = [[ConnectFourBoard.EMPTY_SPACE for i in range(ConnectFourBoard.MAX_Y)] for j in
                       range(ConnectFourBoard.MAX_X)]

    def set_space(self, x, y, val):
        "Sets an individual space"
        if x >= ConnectFourBoard.MAX_X or y >= ConnectFourBoard.MAX_Y:
            raise IndexError

        if type(val) is not int:
            raise TypeError

        if val != ConnectFourBoard.EMPTY_SPACE and val != ConnectFourBoard.PLAYER_MOVE \
        and val != ConnectFourBoard.COMPUTER_MOVE:
            raise ValueError

        self.spaces[x][y] = val

    def get_space(self, x, y):
        "Returns an individual space"
        if x >= ConnectFourBoard.MAX_X or y >= ConnectFourBoard.MAX_Y or x < 0 or y < 0:
            return None
        return self.spaces[x][y]


    def set_board(self, newSpaces):
        """ Replaces the entire ConnectFourBoard.  Check only if the first row is the right length
        does not check values.  Used as a setup shortcut for testing only. """
        if len(newSpaces[1]) != ConnectFourBoard.MAX_Y or len(newSpaces) != ConnectFourBoard.MAX_X:
            raise ValueError
        else:
            self.spaces = newSpaces[:]

    def make_move(self, x, tile):
        """Slides a tile down the selected row.  If the drop worked, a tuple of the
        landing square is returned, else None."""
        if tile != ConnectFourBoard.EMPTY_SPACE and tile != ConnectFourBoard.PLAYER_MOVE \
                and tile != ConnectFourBoard.COMPUTER_MOVE:
            raise ValueError

        if x < 0 or x >= ConnectFourBoard.MAX_X:
            return None

        if self.spaces[x][0] != ConnectFourBoard.EMPTY_SPACE:
            return None

        for y in range(ConnectFourBoard.MAX_Y - 1):
            if self.spaces[x][y + 1] != ConnectFourBoard.EMPTY_SPACE:
                self.set_space(x, y, tile)
                return x, y

        if ConnectFourBoard.EMPTY_SPACE == self.spaces[x][ConnectFourBoard.MAX_Y - 1]:
            self.set_space(x, ConnectFourBoard.MAX_Y - 1, tile)
            return x, ConnectFourBoard.MAX_Y - 1

    def board_full(self):
        for y in range(ConnectFourBoard.MAX_Y):
            for x in range(ConnectFourBoard.MAX_X):
                if self.get_space(x, y) == ConnectFourBoard.EMPTY_SPACE:
                    return False
        return True

    def has_downward_diagonal_winner(self, x, y):
        if x + 3 >= ConnectFourBoard.MAX_X or y + 3 >= ConnectFourBoard.MAX_Y:
            return False
        else:
            return self.get_space(x, y) == self.get_space(x + 1, y + 1)\
                   and self.get_space(x, y) == self.get_space(x + 2, y + 2)\
            and self.get_space(x, y) == self.get_space(x + 3, y + 3)

    def has_upward_diagonal_winner(self, x, y):
        if x + 3 >= ConnectFourBoard.MAX_X or y - 3 < 0:
            return False
        else:
            return self.get_space(x, y) == self.get_space(x + 1, y - 1)\
                   and self.get_space(x, y) == self.get_space(x + 2, y - 2)\
            and self.get_space(x, y) == self.get_space(x + 3, y - 3)

    def has_vertical_winner(self, x, y):
        if y + 3 >= ConnectFourBoard.MAX_Y:
            return False
        else:
            return self.get_space(x, y) == self.get_space(x, y + 1)\
                   and self.get_space(x, y) == self.get_space(x, y + 2)\
            and self.get_space(x, y) == self.get_space(x, y + 3)

    def has_horizontal_winner(self, x, y):
        if x + 3 >= ConnectFourBoard.MAX_X:
            return False
        else:
            return self.get_space(x, y) == self.get_space(x + 1, y)\
                   and self.get_space(x, y) == self.get_space(x + 2, y)\
            and self.get_space(x, y) == self.get_space(x + 3, y)

    def has_winner(self):
        for y in range(ConnectFourBoard.MAX_Y):
            for x in range(ConnectFourBoard.MAX_X):
                if self.spaces[x][y] != ConnectFourBoard.EMPTY_SPACE:
                    if self.get_space(x, y) == self.get_space(x, y + 1):
                        if self.has_vertical_winner(x, y):
                            return self.get_space(x, y)
                    if self.get_space(x, y) == self.get_space(x + 1, y):
                        if self.has_horizontal_winner(x, y):
                            return self.get_space(x, y)
                    if self.get_space(x, y) == self.get_space(x + 1, y + 1):
                        if self.has_downward_diagonal_winner(x, y):
                            return self.get_space(x, y)
                    if self.get_space(x, y) == self.get_space(x + 1, y - 1) and self.has_upward_diagonal_winner(x, y):
                        return self.get_space(x, y)
        return None

    def space_playable(self, x, y):
        if self.get_space(x,y) == self.EMPTY_SPACE and self.get_space(x, y+1) != self.EMPTY_SPACE:
            return True
        else:
            return False
            
    def pretty_print(self):
        "Pretty print of the ConnectFourBoard"
        print "columns  1 2 3 4 5 6 7"
        for y in range(ConnectFourBoard.MAX_Y):
            print "        ",
            for x in range(ConnectFourBoard.MAX_X):
                space = self.get_space(x, y)
                if space == self.COMPUTER_MOVE:
                    print 'C',
                elif space == self.PLAYER_MOVE:
                    print 'P',
                else:
                    print "O",
            print
        return str(self.spaces)

    def __str__(self):
        return str(self.spaces)

if __name__ == "__main__":
    myBoard = ConnectFourBoard()

    myBoard.set_space(5, 3, ConnectFourBoard.PLAYER_MOVE)

    str(myBoard)
    
    