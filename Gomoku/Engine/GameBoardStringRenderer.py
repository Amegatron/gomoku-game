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

        for i in range(board.x):
            result += " " + chr(base_char + i)

        result += "\n"

        for j in range(board.y):
            result += str(j).rjust(2, '0') + ' '
            for i in range(board.x):
                result += self.char_map[board.board[i][j]]
            result += "\n"

        return result
