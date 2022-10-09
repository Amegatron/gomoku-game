from Gomoku.Engine.GameBoard import GameBoard
from Gomoku.Engine.GomokuGame import GomokuGame
import numpy as np


class GomokuEnv:
    def __init__(self, x, y, win_reward=100):
        self.x = x
        self.y = y
        self.win_reward = win_reward
        self.game = GomokuGame(self.x, self.y)

    def reset(self):
        self.game = GomokuGame(self.x, self.y)

        return self.board_to_state(self.game.board)

    def step(self, x, y):
        current_player = self.game.get_current_player()
        result = self.game.make_move(x, y)
        obs = self.board_to_state(self.game.board)
        done = result != 0
        reward = self.win_reward if result == current_player else 0

        return obs, reward, done, None

    def get_allowed_moves_mask(self):
        mask = np.zeros((self.game.board.x, self.game.board.y))

        for i in range(self.game.board.x):
            for j in range(self.game.board.y):
                mask[i][j] = 0 if self.game.board.board[i][j] > 0 else 1

        return mask

    def board_to_state(self, board: GameBoard, current_player=None):
        state = np.zeros((2, board.x, board.y), dtype=np.int)

        if current_player is None:
            current_player = self.game.get_current_player()

        for i in range(board.x):
            for j in range(board.y):
                val = board.board[i][j]

                if val > 0:
                    if val == current_player:
                        state[0][i][j] = 1
                    else:
                        state[1][i][j] = 1

        return state
