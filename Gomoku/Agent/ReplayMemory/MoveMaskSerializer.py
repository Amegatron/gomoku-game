import numpy as np


class MoveMaskSerializer():
    def serialize(self, mask, include_size=False) -> bytearray:
        x = mask.shape[0]
        y = mask.shape[1]
        result = bytearray()

        if include_size:
            result.append(x)
            result.append(y)

        quartet = 0
        counter = 0

        for j in range(y):
            for i in range(x):
                cell_val = mask[i][j]
                val = cell_val << (7 - counter)
                quartet = quartet | val
                counter += 1

                if counter == 8:
                    result.append(quartet)
                    counter = 0
                    quartet = 0

        if counter > 0:
            result.append(quartet)

        return result

    def deserialize(self, data: bytearray, width: int = None, height: int = None):
        start_pos = 0

        if width is None or height is None:
            width = data[0]
            height = data[1]
            start_pos = 2

        result = np.zeros((width, height))

        data_len = len(data)
        for i in range(start_pos, data_len):
            byte = data[i]
            for k in range(8):
                cell_val = (byte >> (7 - k)) & 1
                idx = i*8 + k

                if idx >= width * height:
                    continue

                result[idx % width][idx // width] = cell_val

        return result
