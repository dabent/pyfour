from strategy import C4Easy
from strategy import C4Harder
from board import ConnectFourBoard
import getopt
import sys

FIRST_MOVE = 0
GET_INPUT = 1
COMPUTER_MOVE = 2

def valid_move(move):
    """ Is this a valid move? Currently coded for ConnectFour only.
    possible candidate to move to board/strategy classes."""
    try:
        if int(move)-1 in range(ConnectFourBoard.MAX_X):
            return True
        else:
            return False
    except ValueError:
        return False

def game_runner(state, c4Strategy):
    """Very simple state machine to handle the game itself.
    is passed the initial game state and what strategy to use
    by the caller."""
    
    c4Board = c4Strategy.board

    print " Welcome to Python Connect Four"
    print " Enter a column to make a move..."

    move = None

    while True:

        if state == FIRST_MOVE:
            c4Board.pretty_print()
            state = GET_INPUT
        elif state == GET_INPUT:
            move = raw_input("Make your move (q to quit): ")
            if move == 'q' or move == 'Q':
                break
            else:
                if valid_move(move):
                    if c4Board.make_move(int(move)-1, ConnectFourBoard.PLAYER_MOVE):
                        if c4Board.has_winner():
                            c4Board.pretty_print()
                            print "YOU WON!"
                            break
                        else:
                            state = COMPUTER_MOVE
                else:
                    print "That's an invalid move, try a column number or 'q' to quit"
        elif state == COMPUTER_MOVE:
            c4Strategy.compute_move()
            c4Board.pretty_print()
            if c4Board.has_winner():
                print "COMPUTER WON!"
                break
            else:
                state = GET_INPUT


if __name__ == "__main__":

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hc", ["hard", "computer"])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        print "Usage: -c (computer moves first) -h (turns on hard mode)"
        sys.exit(2)
    output = None
    first_state = FIRST_MOVE
    hard = False
    for o, a in opts:
        if o in ("-h", "--hard"):
            hard = True
        elif o in ("-c", "--computer"):
            first_state = COMPUTER_MOVE
        else:
            assert False, "unhandled option"

    c4Board = ConnectFourBoard()
    c4Strategy = None
    if hard:
        c4Strategy = C4Harder(c4Board)
    else:
        c4Strategy = C4Easy(c4Board)

    game_runner(first_state, c4Strategy)
