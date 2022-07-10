from Gomoku.Agent.ReplayMemory.Contracts.StateSerializerInterface import StateSerializerInterface


class BinaryStateSerializer(StateSerializerInterface):
    """
    Base idea: each byte (8 bits) holds info about 4 consecutive cells on gameboard:
    each pair of bits holds exact cell value: 00, 01, or 10.

    Compacting can also be added here: in general use, there can't be pairs of bits like '11'. So,
    we can use highest '11', for example, as an indicator of a series of zeros, where maximum value
    of the counter can be 63 (the rest 6 bits).

    This serializer is somewhat abandoned, cause TernarySerializer gives out much more compact serialization.
    """
    def serialize(self, state) -> bytearray:
        result = bytearray()
        x = state[0]
        y = state[1]

        result.append(x)
        result.append(y)

        quartet = 0
        counter = 0
        for j in range(x):
            for i in range(y):
                cell_val = 0

                if state[0][i][j] > 0:
                    cell_val = 1
                elif state[1][i][j] > 0:
                    cell_val = 2

                val = cell_val << (3 - counter) * 2
                quartet = quartet | val
                counter += 1

                if counter == 4:
                    result.append(quartet)
                    quartet = 0
                    counter = 0

        return result

    def deserialize(self, data: bytearray):
        raise NotImplementedError("Not implemented yet")
        pass