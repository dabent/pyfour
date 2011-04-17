__author__ = 'Davin'
from board import ConnectFourBoard
import random

class StragegyBase:
    def computeMove(self):
        pass

class C4Easy:
    def __init__(self, board):
        self.board = board

    def findBlock(self):
        self.board.prettyPrint()
        for y in range(ConnectFourBoard.maxY):
            for x in range(ConnectFourBoard.maxX):
                if ConnectFourBoard.playerMove == self.board.spaces[x][y]:
                    #check vertical
                    if self.board.getSpace(x, y) == self.board.getSpace(x, y + 1) == self.board.getSpace(x, y + 2):
                        print "Found it!"
                        if self.board.spacePlayable(x, y-1):
                            print "BLOCK!", x
                            return x
                    #check horizontal
                    if self.board.getSpace(x, y) == self.board.getSpace(x + 1, y) == self.board.getSpace(x+2,y):
                        if self.board.spacePlayable(x-1, y):
                            print "BLOCK!"
                            return x-1
                        if self.board.spacePlayable(x+3, y):
                            print "BLOCK!"
                            return x+3
                    #check horizontal1
                    if self.board.getSpace(x, y) == self.board.getSpace(x + 1, y) == self.board.getSpace(x+3,y):
                        if self.board.spacePlayable(x+2, y):
                            print "BLOCK!"
                            return x+2
                    #check horizontal2
                    if self.board.getSpace(x, y) == self.board.getSpace(x + 2, y) == self.board.getSpace(x+3,y):
                        if self.board.spacePlayable(x+1, y):
                            print "BLOCK!"
                            return x+1
                    #check diagonal1
                    if self.board.getSpace(x, y) == self.board.getSpace(x + 1, y+1) == self.board.getSpace(x+2,y+2):
                        if self.board.spacePlayable(x-1, y-1):
                            print "BLOCK!"
                            return x-1
                        if self.board.spacePlayable(x+3, y+3):
                            print "BLOCK!"
                            return x+3
                    #check diagonal11
                    if self.board.getSpace(x, y) == self.board.getSpace(x + 1, y+1) == self.board.getSpace(x+3,y+3):
                        if self.board.spacePlayable(x+2, y-2):
                            print "BLOCK!"
                            return x+2
                    #check diagonal12
                    if self.board.getSpace(x, y) == self.board.getSpace(x+2, y+2) == self.board.getSpace(x+3,y+3):
                        if self.board.spacePlayable(x-1, y-1):
                            print "BLOCK!"
                            return x-1
                        if self.board.spacePlayable(x+3, y+3):
                            print "BLOCK!"
                            return x+3
                    #check diagonal2
                    if self.board.getSpace(x, y) == self.board.getSpace(x + 1, y-1) == self.board.getSpace(x+2,y-2):
                        if self.board.spacePlayable(x-1, y+1):
                            print "BLOCK!"
                            return x-1
                        if self.board.spacePlayable(x+3, y-3):
                            print "BLOCK!"
                            return x+3
                    #check diagonal21
                    if self.board.getSpace(x, y) == self.board.getSpace(x + 1, y-1) == self.board.getSpace(x+3,y-3):
                        if self.board.spacePlayable(x+2, y+2):
                            print "BLOCK!"
                            return x+2
                    #check diagonal22
                    if self.board.getSpace(x, y) == self.board.getSpace(x+2, y-2) == self.board.getSpace(x+3,y-3):
                        if self.board.spacePlayable(x+1, y+1):
                            print "BLOCK!"
                            return x+1
        return None

    def computeMove(self):
        #go for block
        if self.board.boardFull():
            return False

        move = self.findBlock()

        if move is not None:
            self.board.makeMove(move, ConnectFourBoard.computerMove)
            return True

        move = random.randint(0, ConnectFourBoard.maxX - 1)
        while self.board.makeMove(move, ConnectFourBoard.computerMove) is not None:
            return True
        else:
            move = random.randint(0, ConnectFourBoard.maxX - 1)

    def findThreeAcross(self):
        pass

    def setsUpWin(self):
        pass

    def goForWin(self):
        pass

