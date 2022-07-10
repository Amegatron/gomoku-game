import random
import unittest
import numpy as np

from Gomoku.Agent.ReplayMemory.TernaryStateSerializer import TernaryStateSerializer
from Gomoku.Tests.Agent.ReplayMemory.StateFixture import StateFixture


class MyTestCase(unittest.TestCase):
    def test_serializes(self):
        serializer = TernaryStateSerializer()
        state_fixture = StateFixture()

        with self.subTest("Empty field"):
            state = np.zeros((2, random.randint(10, 20), random.randint(10, 20)))
            serialized_state = serializer.serialize(state)
            deserialized_state = serializer.deserialize(serialized_state)
            self.assertTrue(np.array_equal(state, deserialized_state))

        with self.subTest("Long zero-series with interruption"):
            state = np.zeros((2, 20, 20))
            state[0][10, 10] = 1
            serialized_state = serializer.serialize(state)
            deserialized_state = serializer.deserialize(serialized_state)
            self.assertTrue(np.array_equal(state, deserialized_state))

        for i in range(100):
            with self.subTest("Random field %d" % i):
                state = state_fixture.generate_random_state(random.randint(10, 20), random.randint(10, 20))
                # state = self.__generate_random_state(10, 20)
                serialized_state = serializer.serialize(state)
                deserialized_state = serializer.deserialize(serialized_state)
                if not np.array_equal(state, deserialized_state):
                    a = True

                self.assertTrue(np.array_equal(state, deserialized_state))


if __name__ == '__main__':
    unittest.main()
