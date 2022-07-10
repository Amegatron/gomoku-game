import numpy as np

from Gomoku.Agent.GomokuEnv import GomokuEnv
from Gomoku.Agent.ReplayMemory.TernaryStateSerializer import TernaryStateSerializer
from Gomoku.Engine.GameBoard import GameBoard
from Gomoku.Engine.GameBoardStringRenderer import GameBoardStringRenderer

p1_moves = [[3, 0],
            [4, 0],
            [2, 1],
            [7, 1],
            [1, 2],
            [6, 2],
            [7, 2],
            [8, 2],
            [3, 3],
            [4, 3],
            [7, 3],
            [8, 3],
            [5, 4],
            [6, 4],
            [2, 5],
            [3, 5],
            [4, 5],
            [5, 5]]
p2_moves = [[3, 1],
            [4, 1],
            [5, 1],
            [9, 1],
            [2, 2],
            [3, 2],
            [4, 2],
            [5, 2],
            [1, 3],
            [5, 3],
            [6, 3],
            [3, 4],
            [4, 4],
            [7, 4],
            [1, 5],
            [6, 5],
            [8, 5],
            [4, 6]]

board = GameBoard(10, 10)

for i, move in enumerate(p1_moves):
    board.make_move(move[0], move[1], 2)

for i, move in enumerate(p2_moves):
    board.make_move(move[0], move[1], 1)

renderer = GameBoardStringRenderer()
print(renderer.render(board))

env = GomokuEnv(10, 10)
state = env.board_to_state(board)
serializer = TernaryStateSerializer()
serialized_state = serializer.serialize(state)
deserialized_state = serializer.deserialize(serialized_state)
print(serialized_state)
print(list(serialized_state))
print("%d bytes" % len(serialized_state))
print(np.array_equal(state, deserialized_state))
