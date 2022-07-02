import random
import unittest
from GomokuEnv import GomokuEnv


class MyTestCase(unittest.TestCase):
    def test_empty_initial_observation(self):
        gomoku_env = GomokuEnv(10, 10)
        obs = gomoku_env.reset()
        self.assertEquals(obs.all(), 0)

    def test_step(self):
        gomoku_env = GomokuEnv(10, 10, 100)
        gomoku_env.reset()

        # Before "step", layer "0" is ours (current player, making a step).
        # After "step" the layers are automatically switched

        obs, reward, done, _ = gomoku_env.step(5, 5)
        self.assertFalse(done)
        self.assertEquals(0, reward)
        self.assertEquals(obs[0, :, :].all(), 0)
        self.assertEquals(obs[1][5][5], 1)

        obs, reward, done, _ = gomoku_env.step(5, 4)
        self.assertFalse(done)
        self.assertEquals(0, reward)
        self.assertEquals(obs[0][5][5], 1)  # Previous step
        self.assertEquals(obs[1][5][4], 1)

    def test_reward_and_done(self):
        expected_reward = random.randint(10, 100)
        gomoku_env = GomokuEnv(10, 10, expected_reward)
        gomoku_env.reset()
        gomoku_env.step(0, 0)
        gomoku_env.step(0, 1)
        gomoku_env.step(1, 0)
        gomoku_env.step(1, 1)
        gomoku_env.step(2, 0)
        gomoku_env.step(2, 1)
        gomoku_env.step(3, 0)
        gomoku_env.step(4, 1)
        obs, reward, done, _ = gomoku_env.step(4, 0)

        self.assertEquals(reward, expected_reward)
        self.assertTrue(done)

    def test_allowed_moves_mask(self):
        gomoku_env = GomokuEnv(10, 10)
        mask = gomoku_env.get_allowed_moves_mask()
        self.assertEquals(mask.all(), 1)

        gomoku_env.step(0, 0)
        gomoku_env.step(1, 0)
        gomoku_env.step(5, 6)

        mask = gomoku_env.get_allowed_moves_mask()
        self.assertEquals(0, mask[0, 0])
        self.assertEquals(0, mask[1, 0])
        self.assertEquals(0, mask[5, 6])
        self.assertEquals(1, mask[2, 2])


if __name__ == '__main__':
    unittest.main()
