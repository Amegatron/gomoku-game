import random


class ReplayMemory:
    def __init__(self, limit=None):
        self.memory = []

    def add_sample(self, state, action, reward, next_state, done):
        sample = (state, action, reward, next_state, done)
        self.memory.append(sample)

    def random_sample(self, amount=100):
        return random.sample(self.memory, amount)

    def enumerate(self):
        return enumerate(self.memory)

    def count(self):
        return len(self.memory)
