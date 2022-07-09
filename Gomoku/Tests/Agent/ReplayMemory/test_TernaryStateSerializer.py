import random
import unittest

import numpy as np

from Gomoku.Agent.GomokuEnv import GomokuEnv
from Gomoku.Agent.ReplayMemory.TernaryStateSerializer import TernaryStateSerializer


class MyTestCase(unittest.TestCase):
    def test_serializes(self):
        serializer = TernaryStateSerializer()

        with self.subTest(0):
            state = np.zeros((2, random.randint(10, 20), random.randint(10, 20)))
            serialized_state = serializer.serialize(state)
            deserialized_state = serializer.deserialize(serialized_state)
            self.assertTrue(np.array_equal(state, deserialized_state))

        for i in range(50):
            with self.subTest(i + 1):
                state = self.__generate_random_state(random.randint(10, 20), random.randint(10, 20))
                # state = self.__generate_random_state(10, 20)
                serialized_state = serializer.serialize(state)
                deserialized_state = serializer.deserialize(serialized_state)
                self.assertTrue(np.array_equal(state, deserialized_state))

    def __generate_random_state(self, x, y):
        """
        Generates technically valid random game state of specified sizes. Technically valid means
        that each cell will be in allowed state (0, 1 or 2, mutually exclusive), but those states
        can be impossible in relation to Gomoku (for exampl, the whole board of X's, etc).
        """
        state = np.zeros((2, x, y))
        attempts = random.randint(0, x*y)

        for i in range(attempts):
            layer = random.randint(0, 1)
            rand_x = random.randint(0, x-1)
            rand_y = random.randint(0, y-1)

            if state[0][rand_x, rand_y] == 0 and state[1][rand_x, rand_y] == 0:
                state[layer][rand_x, rand_y] = 1

        return state

if __name__ == '__main__':
    unittest.main()
