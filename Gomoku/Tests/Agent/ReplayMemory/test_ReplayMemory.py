import random
import unittest

from Gomoku.Agent.ReplayMemory.ReplayMemory import ReplayMemory
from Gomoku.Tests.Agent.ReplayMemory.ReplaySampleFixture import ReplaySampleFixture


class MyTestCase(unittest.TestCase):
    def test_add_sample(self):
        memory = ReplayMemory()
        self.assertEqual(0, memory.count())
        fixture = ReplaySampleFixture()
        samples = [fixture.generate_sample(10, 10) for x in range(random.randint(5, 10))]

        for _, sample in enumerate(samples):
            memory.add_sample(sample)

        self.assertEqual(len(samples), memory.count())

    def test_add_samples(self):
        memory = ReplayMemory()
        self.assertEqual(0, memory.count())
        fixture = ReplaySampleFixture()
        samples = [fixture.generate_sample(10, 10) for x in range(random.randint(5, 10))]
        memory.add_samples(samples)

        self.assertEqual(len(samples), memory.count())


if __name__ == '__main__':
    unittest.main()
