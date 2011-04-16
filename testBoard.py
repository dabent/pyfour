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
        dropBoard.setBoard(drop)

        self.assertIsNotNone(dropBoard.makeMove(4, board.BoardBase.computerMove))

        self.assertIsNotNone(dropBoard.makeMove(2, board.BoardBase.computerMove))

        self.assertEqual(dropBoard.makeMove(5, board.BoardBase.computerMove), None)

    def test_boardFull(self):
        full = [[1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1]]
        fullBoard = board.ConnectFourBoard()
        fullBoard.setBoard(full)
        self.assertTrue(fullBoard.boardFull())

    def test_boardNotFull(self):
        empty = [[0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]
        emptyBoard = board.ConnectFourBoard()
        emptyBoard.setBoard(empty)
        self.assertFalse(emptyBoard.boardFull())

    def test_verticalWin(self):
        vertical = [[0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]]
        verticalBoard = board.ConnectFourBoard()
        verticalBoard.setBoard(vertical)
        self.assertEqual(verticalBoard.hasWinner(), 1)

    def test_horizontalWin(self):
        horizontal = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 2, 1, 1, 1],
                      [0, 0, 2, 0, 0, 0],
                      [0, 0, 2, 0, 0, 0],
                      [0, 0, 2, 0, 0, 0]]
        horizontalBoard = board.ConnectFourBoard()
        horizontalBoard.setBoard(horizontal)
        self.assertEqual(horizontalBoard.hasWinner(), 2)

    def test_forwardDiagonalWin(self):
        diagonal = [[0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 2, 1],
                    [0, 0, 0, 2, 0, 0],
                    [0, 0, 2, 0, 0, 0],
                    [0, 2, 0, 0, 0, 0]]
        diagonalBoard = board.ConnectFourBoard()
        diagonalBoard.setBoard(diagonal)
        self.assertEqual(diagonalBoard.hasWinner(), 2)

    def test_backDiagonalWin(self):
        diagonal = [[0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 2, 1, 1, 1],
                    [0, 0, 0, 2, 0, 0],
                    [0, 0, 0, 0, 2, 0],
                    [0, 0, 0, 0, 0, 2]]
        diagonalBoard = board.ConnectFourBoard()
        diagonalBoard.setBoard(diagonal)
        self.assertEqual(diagonalBoard.hasWinner(), 2)

    def test_noWin(self):
        noWin = [[0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 2, 1, 1, 1],
                 [0, 0, 0, 2, 0, 0],
                 [0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 2]]
        noWinBoard = board.ConnectFourBoard()
        noWinBoard.setBoard(noWin)
        self.assertEqual(noWinBoard.boardFull(), False)
        self.assertEqual(noWinBoard.hasWinner(), None)

    def test_win(self):
        win = [[0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 2],
               [0, 0, 2, 1, 1, 1],
               [0, 0, 0, 2, 1, 2],
               [0, 0, 0, 0, 1, 2],
               [0, 0, 0, 0, 0, 2]]
        winBoard = board.ConnectFourBoard()
        winBoard.setBoard(win)
        self.assertEqual(winBoard.boardFull(), False)
        self.assertEqual(winBoard.hasWinner(), 1)

    def test_draw(self):
        draw = [[1, 2, 1, 2, 1, 2],
                [2, 2, 1, 2, 1, 2],
                [1, 1, 1, 2, 2, 2],
                [2, 1, 2, 1, 2, 1],
                [2, 2, 2, 1, 2, 2],
                [1, 2, 1, 2, 1, 1],
                [1, 2, 1, 2, 2, 2]]
        drawBoard = board.ConnectFourBoard()
        drawBoard.setBoard(draw)
        self.assertEqual(drawBoard.boardFull(), True)
        self.assertEqual(drawBoard.hasWinner(), None)

if __name__ == '__main__':
#    unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBoard)
    unittest.TextTestRunner(verbosity=2).run(suite)

