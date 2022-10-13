import random
import unittest

import numpy as np

from Gomoku.Agent.ReplayMemory.MoveMaskSerializer import MoveMaskSerializer


class MyTestCase(unittest.TestCase):
    def test_serializes_and_deserizliaes(self):
        serializer = MoveMaskSerializer()
        width = random.randint(5, 10)
        height = random.randint(5, 10)
        mask = np.zeros((width, height), dtype=np.int)

        for i in range(random.randint(10, 20)):
            x_ = random.randint(0, width - 1)
            y_ = random.randint(0, height - 1)
            mask[x_][y_] = 1

        data = serializer.serialize(mask, False)
        deserialized_data = serializer.deserialize(data, width, height)
        self.assertTrue(np.array_equal(mask, deserialized_data))

    def test_includes_size(self):
        serializer = MoveMaskSerializer()
        width = random.randint(5, 10)
        height = random.randint(5, 10)
        mask = np.zeros((width, height), dtype=np.int)

        data = serializer.serialize(mask, True)
        deserialized_data = serializer.deserialize(data)
        self.assertTrue(np.array_equal(mask, deserialized_data))


if __name__ == '__main__':
    unittest.main()
