from Gomoku.Agent.ReplayMemory.Contracts.StateSerializerInterface import StateSerializerInterface


class BinaryStateSerializer(StateSerializerInterface):
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