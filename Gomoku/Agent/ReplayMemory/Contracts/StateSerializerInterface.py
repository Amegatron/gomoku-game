class StateSerializerInterface:
    def serialize(self, state, include_size=False):
        pass

    def deserialize(self, data: bytearray, width: int = None, height: int = None):
        pass