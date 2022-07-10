import numpy as np

from Gomoku.Agent.ReplayMemory.Contracts.StateSerializerInterface import StateSerializerInterface


class TernaryStateSerializer(StateSerializerInterface):
    def serialize(self, state) -> bytearray:
        result = bytearray()
        x = state.shape[1]
        y = state.shape[2]

        result.append(x)
        result.append(y)
        zeros_counter = 0
        quartet = ""
        counter = 0

        for j in range(y):
            for i in range(x):
                if state[0][i][j] > 0:
                    cell_val = 1
                elif state[1][i][j] > 0:
                    cell_val = 2
                else:
                    cell_val = 0

                append_zero_series = False

                if cell_val == 0:
                    zeros_counter += 1
                    if zeros_counter >= 127:
                        append_zero_series = True
                elif zeros_counter >= 4:
                    append_zero_series = True
                else:
                    zeros_counter = 0

                if append_zero_series:
                    zero_series_byte = (1 << 7) + zeros_counter
                    result.append(zero_series_byte)
                    zeros_counter = 0
                    quartet = ""
                    counter = 0

                if zeros_counter <= 4:
                    counter += 1
                    quartet = str(cell_val) + quartet
                else:
                    counter = 0
                    quartet = ""

                if counter == 4 and zeros_counter < 4:
                    counter = 0
                    zeros_counter = 0
                    result.append(int(quartet, 3))
                    quartet = ""

        if counter > 0:
            if zeros_counter > 4:
                result.append((1 << 7) + zeros_counter)
            else:
                result.append(int(quartet, 3))

        return result

    def deserialize(self, data: bytearray):
        x = data[0]
        y = data[1]

        state = np.zeros((2, x, y))
        counter = 0

        for i, byte in enumerate(data):
            if i < 2:
                continue

            # zero-series
            if byte & (1 << 7):
                zero_series = byte & (0xff >> 1)
                counter += zero_series
            else:
                temp_byte = byte
                for k in range(4):
                    cell_val = temp_byte % 3
                    temp_byte //= 3
                    layer = None

                    if cell_val == 1:
                        layer = 0
                    elif cell_val == 2:
                        layer = 1

                    if layer is not None:
                        state[layer][counter % x][counter // x] = 1

                    counter += 1

        return state
