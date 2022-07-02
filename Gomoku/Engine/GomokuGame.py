from Gomoku.Engine.GameBoard import GameBoard
from Gomoku.Engine.GomokuRuleSet import GomokuRuleSet


class GomokuGame:
    def __init__(self, width, height, starting_player=1):
        self.board = GameBoard(width, height)
        self.rule_set = GomokuRuleSet()
        self.current_player = starting_player - 1

    def make_move(self, x, y):
        player_num = self.current_player + 1
        if self.can_make_move(x, y):
            self.board.make_move(x, y, player_num)
            self.current_player = player_num % 2
        else:
            raise AssertionError("Can not make move to this cell")

        return self.rule_set.check_game_ended(self.board)

    def can_make_move(self, x, y):
        return self.rule_set.can_place(self.board, x, y)

    def get_current_player(self):
        return self.current_player + 1
