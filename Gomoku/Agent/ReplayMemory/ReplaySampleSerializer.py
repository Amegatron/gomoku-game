from Gomoku.Agent.ReplayMemory.Contracts.ReplaySampleSerializerInterface import ReplaySampleSerializerInterface
from Gomoku.Agent.ReplayMemory.MoveMaskSerializer import MoveMaskSerializer
from Gomoku.Agent.ReplayMemory.ReplaySample import ReplaySample
from Gomoku.Agent.ReplayMemory.Contracts.StateSerializerInterface import StateSerializerInterface

BYTEORDER = "little"


class ReplaySampleSerializer(ReplaySampleSerializerInterface):
    def __init__(self, state_serializer: StateSerializerInterface):
        self.state_serializer = state_serializer
        self.mask_serializer = MoveMaskSerializer()

    def serialize(self, sample: ReplaySample) -> bytearray:
        result = bytearray()

        result.append(sample.state.shape[1])
        result.append(sample.state.shape[2])

        serialized_state = self.state_serializer.serialize(sample.state, include_size=False)
        result += len(serialized_state).to_bytes(2, BYTEORDER)
        result += serialized_state

        serialized_mask = self.mask_serializer.serialize(sample.move_mask, include_size=False)
        result += len(serialized_mask).to_bytes(2, BYTEORDER)
        result += serialized_mask

        serialized_next_state = self.state_serializer.serialize(sample.next_state, include_size=False)
        result += len(serialized_next_state).to_bytes(2, BYTEORDER)
        result += serialized_next_state

        result.append(sample.action[0])
        result.append(sample.action[1])
        result.append(sample.reward)
        result.append(ord("0") + int(sample.done))

        return result

    def deserialize(self, data: bytearray) -> ReplaySample:
        width = data[0]
        height = data[1]
        pos = 2

        len1 = int.from_bytes(data[pos:(pos + 1)], BYTEORDER)
        pos += 2
        state_bytes = data[pos:(pos + len1)]
        state = self.state_serializer.deserialize(state_bytes, width, height)
        pos += len1

        len2 = int.from_bytes(data[pos:(pos + 1)], BYTEORDER)
        pos += 2
        mask_bytes = data[pos:(pos + len2)]
        mask = self.mask_serializer.deserialize(mask_bytes, width, height)
        pos += len2

        len3 = int.from_bytes(data[pos:(pos + 1)], BYTEORDER)
        pos += 2
        next_state_bytes = data[pos:(pos + len3)]
        next_state = self.state_serializer.deserialize(next_state_bytes, width, height)
        pos += len3

        action = (data[pos], data[pos + 1])
        pos += 2
        reward = data[pos]
        pos += 1
        done_raw = data[pos]
        done = bool(done_raw - ord("0"))

        return ReplaySample(state, action, reward, next_state, done, mask)
