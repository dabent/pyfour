__author__ = 'Davin'
import unittest
import board
import strategy

class TestStrategy(unittest.TestCase):
    def setUp(self):
        pass

    def test_diagonal_win(self):
        dWin = [[0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 2, 1, 1, 1],
                 [0, 0, 0, 2, 2, 1],
                 [0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 2]]
        dBoard = board.ConnectFourBoard()
        dBoard.set_board(dWin)
        c4HardStrategy = strategy.C4Harder(dBoard)
        self.assertTrue(c4HardStrategy.find_group_of_three(dBoard.COMPUTER_MOVE))

if __name__ == '__main__':
#    unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStrategy)
    unittest.TextTestRunner(verbosity=2).run(suite)

