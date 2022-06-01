import unittest

from GameBoard import GameBoard
from GomokuRuleSet import GomokuRuleSet


class GomokuRuleSetTest(unittest.TestCase):
    def test_game_ended(self):
        rule_set = GomokuRuleSet()
        boards = self._get_test_game_boards()
        for i, board_data in enumerate(boards):
            with self.subTest(i):
                board = board_data[0]
                result = board_data[1]
                self.assertEquals(result, rule_set.check_game_ended(board))

    def _get_test_game_boards(self):
        boards = []

        board1 = GameBoard(10, 10)
        board2 = GameBoard(10, 10)
        board3 = GameBoard(10, 10)
        board4 = GameBoard(10, 10)
        board5 = GameBoard(10, 10)
        board6 = GameBoard(10, 10)

        for i in range(5):
            board1.make_move(1, i, 1)
            board2.make_move(i, 1, 2)
            board3.make_move(8, i, 2)
            board4.make_move(i, 8, 1)
            board5.make_move(i, i, 1)
            board6.make_move(i+2, 8-i, 2)

        boards.append((board1, 1))
        boards.append((board2, 2))
        boards.append((board3, 2))
        boards.append((board4, 1))
        boards.append((board5, 1))
        boards.append((board6, 2))

        board1 = GameBoard(10, 10)
        board2 = GameBoard(10, 10)
        board3 = GameBoard(10, 10)
        board4 = GameBoard(10, 10)
        board5 = GameBoard(10, 10)
        board6 = GameBoard(10, 10)

        for i in range(4):
            board1.make_move(1, i, 2)
            board2.make_move(i, 1, 1)
            board3.make_move(8, i, 2)
            board4.make_move(i, 8, 2)
            board5.make_move(i, i, 1)
            board6.make_move(i+2, 8-i, 2)

        boards.append((board1, 0))
        boards.append((board2, 0))
        boards.append((board3, 0))
        boards.append((board4, 0))
        boards.append((board5, 0))
        boards.append((board6, 0))

        board = GameBoard(10, 10)
        boards.append((board, 0))

        """
          XOXOXOXO
          XOXOXOXO
          OXOXOXOX
          OXOXOXOX
          ...
        """
        board1 = GameBoard(10, 10)
        board2 = GameBoard(10, 10)
        for i in range(10):
            for j in range(5):
                player = (i % 2 + j % 2) % 2 + 1
                board1.make_move(i, j*2, player)
                board1.make_move(i, j*2 + 1, player)

                board2.make_move(j*2, i, player)
                board2.make_move(j*2 + 1, i, player)

        boards.append((board1, -1))
        boards.append((board2, -1))

        return boards


if __name__ == '__main__':
    unittest.main()
