from strategy import C4Easy
from board import ConnectFourBoard

__author__ = 'Davin'

def game_runner():
    c4Board = ConnectFourBoard()
    c4Strategy = C4Easy(c4Board)

    print " Welcome to Python Connect Four"
    print " Enter a column to make a move..."
    c4Board.pretty_print()

    while True:
        move = raw_input("Make your move (q to quit): ")

        if move != 'q':
            if c4Board.make_move(int(move)-1, ConnectFourBoard.PLAYER_MOVE):
                if c4Board.has_winner():
                    c4Board.pretty_print()
                    print "YOU WON!"
                    break
            else:
                print "BAD MOVE"
        else:
            print "Game terminated."
            break
            #Computer's turn
        c4Strategy.compute_move()
        c4Board.pretty_print()
        if c4Board.has_winner():
            print "COMPUTER WON!"
            break

if __name__ == "__main__":
    game_runner()

