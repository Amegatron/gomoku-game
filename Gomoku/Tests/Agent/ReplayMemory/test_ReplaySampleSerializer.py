import unittest

import numpy as np

from Gomoku.Agent.ReplayMemory.ReplaySampleSerializer import ReplaySampleSerializer
from Gomoku.Agent.ReplayMemory.TernaryStateSerializer import TernaryStateSerializer
from Gomoku.Tests.Agent.ReplayMemory.ReplaySampleFixture import ReplaySampleFixture


class MyTestCase(unittest.TestCase):
    def test_serializer(self):
        fixture = ReplaySampleFixture()
        serializer = ReplaySampleSerializer(TernaryStateSerializer())

        for i in range(100):
            with self.subTest(i):
                sample = fixture.generate_sample()
                serialized_sample = serializer.serialize(sample)
                restored_sample = serializer.deserialize(serialized_sample)

                self.assertTrue(np.array_equal(sample.state, restored_sample.state))
                self.assertTrue(np.array_equal(sample.next_state, restored_sample.next_state))
                self.assertEqual(sample.reward, restored_sample.reward)
                self.assertEqual(sample.done, restored_sample.done)
                self.assertEqual(sample.action, restored_sample.action)


if __name__ == '__main__':
    unittest.main()
