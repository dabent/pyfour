__author__ = 'Davin'
from board import ConnectFourBoard
import random

class StragegyBase:
    def compute_move(self):
        pass

class C4Easy(StragegyBase):
    def __init__(self, board):
        self.board = board

    def find_group_of_three(self, player):
        for y in range(ConnectFourBoard.MAX_Y):
            for x in range(ConnectFourBoard.MAX_X):
                if player == self.board.spaces[x][y]:
                    #check vertical
                    if self.board.get_space(x, y) == self.board.get_space(x, y + 1) == self.board.get_space(x, y + 2):
                        print "Found it!"
                        if self.board.space_playable(x, y-1):
                            print "BLOCK!", x
                            return x
                    #check horizontal
                    if self.board.get_space(x, y) == self.board.get_space(x + 1, y) == self.board.get_space(x+2,y):
                        if self.board.space_playable(x-1, y):
                            print "BLOCK!"
                            return x-1
                        if self.board.space_playable(x+3, y):
                            print "BLOCK!"
                            return x+3
                    #check horizontal1
                    if self.board.get_space(x, y) == self.board.get_space(x + 1, y) == self.board.get_space(x+3,y):
                        if self.board.space_playable(x+2, y):
                            print "BLOCK!"
                            return x+2
                    #check horizontal2
                    if self.board.get_space(x, y) == self.board.get_space(x + 2, y) == self.board.get_space(x+3,y):
                        if self.board.space_playable(x+1, y):
                            print "BLOCK!"
                            return x+1
                    #check diagonal1
                    if self.board.get_space(x, y) == self.board.get_space(x + 1, y+1) == self.board.get_space(x+2,y+2):
                        if self.board.space_playable(x-1, y-1):
                            print "BLOCK!"
                            return x-1
                        if self.board.space_playable(x+3, y+3):
                            print "BLOCK!"
                            return x+3
                    #check diagonal11
                    if self.board.get_space(x, y) == self.board.get_space(x + 1, y+1) == self.board.get_space(x+3,y+3):
                        if self.board.space_playable(x+2, y-2):
                            print "BLOCK!"
                            return x+2
                    #check diagonal12
                    if self.board.get_space(x, y) == self.board.get_space(x+2, y+2) == self.board.get_space(x+3,y+3):
                        if self.board.space_playable(x-1, y-1):
                            print "BLOCK!"
                            return x-1
                        if self.board.space_playable(x+3, y+3):
                            print "BLOCK!"
                            return x+3
                    #check diagonal2
                    if self.board.get_space(x, y) == self.board.get_space(x + 1, y-1) == self.board.get_space(x+2,y-2):
                        if self.board.space_playable(x-1, y+1):
                            print "BLOCK!"
                            return x-1
                        if self.board.space_playable(x+3, y-3):
                            print "BLOCK!"
                            return x+3
                    #check diagonal21
                    if self.board.get_space(x, y) == self.board.get_space(x + 1, y-1) == self.board.get_space(x+3,y-3):
                        if self.board.space_playable(x+2, y+2):
                            print "BLOCK!"
                            return x+2
                    #check diagonal22
                    if self.board.get_space(x, y) == self.board.get_space(x+2, y-2) == self.board.get_space(x+3,y-3):
                        if self.board.space_playable(x+1, y+1):
                            print "BLOCK!"
                            return x+1
        return None

    def compute_move(self):
        """ Goes for the win, then the block, then gives up and tries a
        random move until it finds a spot. """
        
        #go for block
        if self.board.board_full():
            return False

        #go for the win!
        move = self.find_group_of_three(ConnectFourBoard.COMPUTER_MOVE)
        if move is None:
            #no win?  Try for a block
            move = self.find_group_of_three(ConnectFourBoard.PLAYER_MOVE)

        if move is not None:
            self.board.make_move(move, ConnectFourBoard.COMPUTER_MOVE)
            return True
        else:
            move = random.randint(0, ConnectFourBoard.MAX_X - 1)
            while self.board.make_move(move, ConnectFourBoard.COMPUTER_MOVE) is not None:
                return True
            else:
                move = random.randint(0, ConnectFourBoard.MAX_X - 1)

    def sets_up_win(self):
        pass

    def go_for_win(self):
        pass

