import random


class ReplayMemory:
    def __init__(self, limit=None):
        self.memory = []

    def add_sample(self, sample):
        self.memory.append(sample)

    def add_samples(self, samples):
        for _, sample in enumerate(samples):
            self.memory.append(sample)

    def random_sample(self, amount=100):
        return random.sample(self.memory, amount)

    def enumerate(self):
        return enumerate(self.memory)

    def count(self):
        return len(self.memory)
