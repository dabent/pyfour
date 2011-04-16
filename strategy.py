__author__ = 'Davin'
from board import ConnectFourBoard
import random

class StragegyBase:
    def computeMove(self):
        pass


class C4Easy:
    def computeMove(self, board):
        #go for block
        if board.boardFull():
            return False

        move = random.randint(0, ConnectFourBoard.maxX - 1)
        while board.makeMove(move, ConnectFourBoard.computerMove) is not None:
            return True
        else:
            move = random.randint(0, ConnectFourBoard.maxX - 1)

    def findThreeAcross(self):
        pass

    def playableSpot(self):
        pass

    def findBlock(self, board):
        self.findThreeAcross()
        self.playableSpot()
        pass

    def setsUpWin(self):
        pass

    def goForWin(self):
        pass