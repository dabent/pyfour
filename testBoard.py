import unittest
import board

__author__ = 'Davin'

class TestBoard(unittest.TestCase):
    def setUp(self):
        pass

    def  test_drop(self):
        drop = [[1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1],
                [0, 0, 0, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1]]

        dropBoard = board.ConnectFourBoard()
        dropBoard.set_board(drop)

        self.assertIsNotNone(dropBoard.make_move(4, board.BoardBase.COMPUTER_MOVE))

        self.assertIsNotNone(dropBoard.make_move(2, board.BoardBase.COMPUTER_MOVE))

        self.assertEqual(dropBoard.make_move(5, board.BoardBase.COMPUTER_MOVE), None)

    def test_board_full(self):
        full = [[1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1]]
        fullBoard = board.ConnectFourBoard()
        fullBoard.set_board(full)
        self.assertTrue(fullBoard.board_full())

    def test_board_not_full(self):
        empty = [[0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]
        emptyBoard = board.ConnectFourBoard()
        emptyBoard.set_board(empty)
        self.assertFalse(emptyBoard.board_full())

    def test_vertical_win(self):
        vertical = [[0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]]
        verticalBoard = board.ConnectFourBoard()
        verticalBoard.set_board(vertical)
        self.assertEqual(verticalBoard.has_winner(), 1)

    def test_horizontal_win(self):
        horizontal = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 2, 1, 1, 1],
                      [0, 0, 2, 0, 0, 0],
                      [0, 0, 2, 0, 0, 0],
                      [0, 0, 2, 0, 0, 0]]
        horizontalBoard = board.ConnectFourBoard()
        horizontalBoard.set_board(horizontal)
        self.assertEqual(horizontalBoard.has_winner(), 2)

    def test_forward_diagonal_win(self):
        diagonal = [[0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 2, 1],
                    [0, 0, 0, 2, 0, 0],
                    [0, 0, 2, 0, 0, 0],
                    [0, 2, 0, 0, 0, 0]]
        diagonalBoard = board.ConnectFourBoard()
        diagonalBoard.set_board(diagonal)
        self.assertEqual(diagonalBoard.has_winner(), 2)

    def test_back_diagonal_win(self):
        diagonal = [[0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 2, 1, 1, 1],
                    [0, 0, 0, 2, 0, 0],
                    [0, 0, 0, 0, 2, 0],
                    [0, 0, 0, 0, 0, 2]]
        diagonalBoard = board.ConnectFourBoard()
        diagonalBoard.set_board(diagonal)
        self.assertEqual(diagonalBoard.has_winner(), 2)

    def test_no_win(self):
        noWin = [[0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 2, 1, 1, 1],
                 [0, 0, 0, 2, 0, 0],
                 [0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 2]]
        noWinBoard = board.ConnectFourBoard()
        noWinBoard.set_board(noWin)
        self.assertEqual(noWinBoard.board_full(), False)
        self.assertEqual(noWinBoard.has_winner(), None)

    def test_win(self):
        win = [[0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 2],
               [0, 0, 2, 1, 1, 1],
               [0, 0, 0, 2, 1, 2],
               [0, 0, 0, 0, 1, 2],
               [0, 0, 0, 0, 0, 2]]
        winBoard = board.ConnectFourBoard()
        winBoard.set_board(win)
        self.assertEqual(winBoard.board_full(), False)
        self.assertEqual(winBoard.has_winner(), 1)

    def test_draw(self):
        draw = [[1, 2, 1, 2, 1, 2],
                [2, 2, 1, 2, 1, 2],
                [1, 1, 1, 2, 2, 2],
                [2, 1, 2, 1, 2, 1],
                [2, 2, 2, 1, 2, 2],
                [1, 2, 1, 2, 1, 1],
                [1, 2, 1, 2, 2, 2]]
        drawBoard = board.ConnectFourBoard()
        drawBoard.set_board(draw)
        self.assertEqual(drawBoard.board_full(), True)
        self.assertEqual(drawBoard.has_winner(), None)

if __name__ == '__main__':
#    unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBoard)
    unittest.TextTestRunner(verbosity=2).run(suite)

