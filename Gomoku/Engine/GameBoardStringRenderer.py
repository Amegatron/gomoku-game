from Gomoku.Engine.GameBoard import GameBoard


class GameBoardStringRenderer:
    default_char_map = (" •", " X", " O")

    def __init__(self, char_map=None):
        if char_map is None:
            char_map = self.default_char_map

        self.char_map = char_map

    def render(self, board: GameBoard):
        result = "   "
        base_char = ord("A")
        max_char = ord("Z")
        range_len = max_char - base_char

        for i in range(board.x):
            if i <= range_len:
                result += " " + chr(base_char + i)
            else:
                result += " " + chr(base_char + i - range_len - 1).lower()

        result += "\n"

        for j in range(board.y):
            result += str(j).rjust(2, '0') + ' '
            for i in range(board.x):
                result += self.char_map[board.board[i][j]]
            result += "\n"

        return result
