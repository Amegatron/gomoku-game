from Gomoku.Agent.ReplayMemory.ReplaySample import ReplaySample


class ReplaySampleSerializerInterface:
    def serialize(self, sample: ReplaySample) -> bytearray:
        pass

    def deserialize(self, data: bytearray) -> ReplaySample:
        pass