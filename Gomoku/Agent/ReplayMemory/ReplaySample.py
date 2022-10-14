"""
Represents a single replay memory sample
"""


class ReplaySample:
    def __init__(self, state, action, reward, next_state, done, move_mask):
        self.state = state
        self.action = action
        self.reward = reward
        self.next_state = next_state
        self.done = done
        self.move_mask = move_mask
