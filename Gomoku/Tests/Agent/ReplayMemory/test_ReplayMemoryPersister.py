import os.path
import random
import unittest

from Gomoku.Agent.ReplayMemory.Drivers.InMemoryIoDriver import InMemoryIoDriver
from Gomoku.Agent.ReplayMemory.ReplayMemoryPersister import ReplayMemoryPersister


class MyTestCase(unittest.TestCase):
    def test_saving_and_loading(self):
        slot_name = "test_slot1"
        samples_num = random.randint(5, 10)

        persister = ReplayMemoryPersister(InMemoryIoDriver())
        samples = [self.__get_ramdom_sample(random.randint(10, 20)) for x in range(samples_num)]
        persister.save(samples, slot_name)

        loaded_samples = persister.load(slot_name)
        self.assertCountEqual(samples, loaded_samples)

        for i in range(len(loaded_samples)):
            self.assertEqual(samples[i], loaded_samples[i])

    def __get_ramdom_sample(self, len):
        sample = bytearray()
        for i in range(len):
            sample.append(random.randint(0, 255))

        return sample

if __name__ == '__main__':
    unittest.main()
