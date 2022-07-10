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


if __name__ == '__main__':
    unittest.main()
