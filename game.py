from strategy import C4Easy
from board import ConnectFourBoard

__author__ = 'Davin'

def gameRunner():
    c4Board = ConnectFourBoard()
    c4Strategy = C4Easy(c4Board)

    print " Welcome to Python Connect Four"
    print " Enter a column to make a move..."
    c4Board.prettyPrint()

    while True:
        move = raw_input("Make your move (q to quit): ")

        if move != 'q':
            if c4Board.makeMove(int(move)-1, ConnectFourBoard.playerMove):
                if c4Board.hasWinner():
                    c4Board.prettyPrint()
                    print "YOU WON!"
                    break
            else:
                print "BAD MOVE"
        else:
            print "Game terminated."
            break
            #Computer's turn
        c4Strategy.computeMove()
        c4Board.prettyPrint()
        if c4Board.hasWinner():
            print "COMPUTER WON!"
            break

if __name__ == "__main__":
    gameRunner()

