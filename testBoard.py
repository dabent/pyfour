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

        self.assertIsNotNone(dropBoard.makeMove(4,board.BoardBase.computerMove))

        self.assertIsNotNone(dropBoard.makeMove(2,board.BoardBase.computerMove))

        self.assertEqual(dropBoard.makeMove(5,board.BoardBase.computerMove), None)

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

    def test_win(self):
        pass

    def test_draw(self):
        pass

    