import unittest

import torch

from Gomoku.Agent.GomokuEnv import GomokuEnv
from Gomoku.Agent.GomokuModel import GomokuModel


class MyTestCase(unittest.TestCase):
    def test_model(self):
        size = 19
        env = GomokuEnv(size, size)
        model = GomokuModel(size, size)

        states = []
        masks = []
        batch_size = 2
        for i in range(batch_size):
            masks.append(env.get_allowed_moves_mask())
            step_result = env.step(i, 0)
            states.append(step_result[0])

        states_tensor = torch.tensor(states, dtype=torch.float)
        masks_tensor = torch.tensor(masks)
        moves = model(states_tensor, masks_tensor)
        self.assertEqual(batch_size, moves.shape[0])
        self.assertEqual(size, moves.shape[1])
        self.assertEqual(size, moves.shape[2])


if __name__ == '__main__':
    unittest.main()
