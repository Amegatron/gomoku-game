import random
import unittest
import numpy as np

from Gomoku.Agent.ReplayMemory.TernaryStateSerializer import TernaryStateSerializer
from Gomoku.Tests.Agent.ReplayMemory.StateFixture import StateFixture


class MyTestCase(unittest.TestCase):
    def test_serializes(self):
        serializer = TernaryStateSerializer()
        state_fixture = StateFixture()
        width = random.randint(10, 20)
        height = random.randint(10, 20)

        with self.subTest("Empty field"):
            state = np.zeros((2, width, height))
            serialized_state = serializer.serialize(state)
            deserialized_state = serializer.deserialize(serialized_state, width, height)
            self.assertTrue(np.array_equal(state, deserialized_state))

        with self.subTest("Long zero-series with interruption"):
            state = np.zeros((2, 20, 20))
            state[0][10, 10] = 1
            serialized_state = serializer.serialize(state)
            deserialized_state = serializer.deserialize(serialized_state, 20, 20)
            self.assertTrue(np.array_equal(state, deserialized_state))

        for i in range(100):
            with self.subTest("Random field %d" % i):
                state, _ = state_fixture.generate_random_state(width, height)
                # state = self.__generate_random_state(10, 20)
                serialized_state = serializer.serialize(state)
                deserialized_state = serializer.deserialize(serialized_state, width, height)
                if not np.array_equal(state, deserialized_state):
                    a = True

                self.assertTrue(np.array_equal(state, deserialized_state))


if __name__ == '__main__':
    unittest.main()
