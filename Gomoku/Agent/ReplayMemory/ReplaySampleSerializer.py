"""
Serializes replay memory sample
"""
from Gomoku.Agent.ReplayMemory.ReplaySample import ReplaySample


class ReplaySampleSerializer:
    def serialize(self, sample: ReplaySample) -> bytearray:
        result = bytearray()
        result += self.__serialize_state(sample.state)
        result += ord(";")
        result += self.__serialize_state(sample.next_state)
        result += ord(";")
        result += [sample.action[0], ord(","), sample.action[1]]
        result += ord(";")
        result += ord("1") if sample.done else ord("0")

        return result

    def deserialize(self, bytes: bytearray) -> ReplaySample:
        pass

