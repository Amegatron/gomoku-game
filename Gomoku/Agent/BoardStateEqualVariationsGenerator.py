import numpy as np

"""
    Class is used to generate identical states from a given state.
    Specifically: 3 90-degree rotations, horizontal, vertical and diagonal flips
    
    Note, that this generator does not guarantee uniqueness of returned states. For example,
    if initial state is already symmetrical along vertical axis, it's corresponding flipped version
    will still be returned
"""


class BoardStateEqualVariationsGenerator:
    def get_variations(self, state):
        rot180 = np.rot90(state, 2, (1, 2))
        variations = np.stack([
            state,
            np.rot90(state, 1, (1, 2)),
            rot180,
            np.rot90(state, 3, (1, 2)),
            np.flip(state, 1),
            np.flip(state, 2),
            np.transpose(state, (0, 2, 1)),
            np.transpose(rot180, (0, 2, 1)),
        ])

        return variations
