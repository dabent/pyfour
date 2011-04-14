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

        dropBoard = board.Board()
        dropBoard.setBoard(drop)

        self.assertIsNotNone(dropBoard.dropTile(4,board.Board.computerMove))

        self.assertIsNotNone(dropBoard.dropTile(2,board.Board.computerMove))

        self.assertEqual(dropBoard.dropTile(5,board.Board.computerMove), None)

    def test_boardFull(self):
        full = [[1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1]]
        fullBoard = board.Board();
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
        emptyBoard = board.Board();
        emptyBoard.setBoard(empty)
        self.assertFalse(emptyBoard.boardFull())

    def test_win(self):
        pass

    def test_draw(self):
        pass

    