import random

import numpy as np

from Gomoku.Agent.ReplayMemory.ReplaySample import ReplaySample
from Gomoku.Tests.Agent.ReplayMemory.StateFixture import StateFixture


class ReplaySampleFixture:
    def generate_sample(self, x=None, y=None):
        x = random.randint(10, 20) if x is None else x
        y = random.randint(10, 20) if y is None else y

        state_fixture = StateFixture()
        state, mask = state_fixture.generate_random_state(x, y)
        next_state, _ = state_fixture.generate_random_state(x, y)
        action_x = random.randint(0, x - 1)
        action_y = random.randint(0, y - 1)
        reward = random.randint(0, 100)
        done = bool(random.randint(0, 1))

        return ReplaySample(state, (action_x, action_y), reward, next_state, done, mask)
