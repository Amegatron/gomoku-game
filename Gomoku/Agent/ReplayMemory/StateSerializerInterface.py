class StateSerializerInterface:
    def serialize(self, state):
        pass

    def deserialize(self, data: bytearray):
        pass