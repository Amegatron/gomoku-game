import unittest
from Gomoku.Engine.GameBoard import GameBoard
from Gomoku.Engine.GameBoardSerializer import GameBoardSerializer


class MyTestCase(unittest.TestCase):
    def test_something(self):
        board = GameBoard(10, 10)
        board.make_move(0, 0, 1)
        board.make_move(1, 0, 2)
        board.make_move(2, 0, 1)
        board.make_move(3, 0, 2)

        board.make_move(0, 1, 1)
        board.make_move(1, 1, 1)
        board.make_move(2, 1, 1)
        board.make_move(3, 1, 1)

        serializer = GameBoardSerializer()
        result = serializer.serialize(board)

        self.assertEquals(len(result), 2+10*10/4)

        self.assertEquals(result[0], 10)
        self.assertEquals(result[1], 10)

        self.assertEquals(result[2], 0b01100110)
        self.assertEquals(result[3], 0)

        self.assertEquals(result[4], 0b00000101)
        self.assertEquals(result[5], 0b01010000)


if __name__ == '__main__':
    unittest.main()
