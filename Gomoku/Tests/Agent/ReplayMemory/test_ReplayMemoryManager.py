import copy
import random
import unittest

from Gomoku.Agent.ReplayMemory.Drivers.InMemoryIoDriver import InMemoryIoDriver
from Gomoku.Agent.ReplayMemory.ReplayMemory import ReplayMemory
from Gomoku.Agent.ReplayMemory.ReplayMemoryManager import ReplayMemoryManager
from Gomoku.Agent.ReplayMemory.ReplayMemoryPersister import ReplayMemoryPersister
from Gomoku.Agent.ReplayMemory.ReplaySampleSerializer import ReplaySampleSerializer
from Gomoku.Agent.ReplayMemory.TernaryStateSerializer import TernaryStateSerializer
from Gomoku.Tests.Agent.ReplayMemory.ReplaySampleFixture import ReplaySampleFixture


class MyTestCase(unittest.TestCase):
    def test_unique(self):
        persister = ReplayMemoryPersister(InMemoryIoDriver())
        manager = ReplayMemoryManager(persister, ReplaySampleSerializer(TernaryStateSerializer()))
        memory = ReplayMemory()
        fixture = ReplaySampleFixture()
        sample1 = fixture.generate_sample(10, 10)
        sample2 = fixture.generate_sample(10, 10)
        memory.add_sample(sample1)
        memory.add_sample(sample2)

        for i in range(random.randint(5, 10)):
            memory.add_sample(copy.deepcopy(sample1))
            memory.add_sample(copy.deepcopy(sample2))

        test_memory = manager.unique(memory)
        self.assertEqual(2, test_memory.count())

    def test_save_load(self):
        persister = ReplayMemoryPersister(InMemoryIoDriver())
        manager = ReplayMemoryManager(persister, ReplaySampleSerializer(TernaryStateSerializer()))
        memory = ReplayMemory()
        fixture = ReplaySampleFixture()

        for i in range(random.randint(5, 10)):
            memory.add_sample(fixture.generate_sample(10, 10))

        save_name = "test_name"
        manager.save(memory, save_name)
        test_memory = manager.load(save_name)

        self.assertEqual(memory.count(), test_memory.count())


if __name__ == '__main__':
    unittest.main()
