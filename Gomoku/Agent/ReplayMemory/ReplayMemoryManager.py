import base64

from Gomoku.Agent.ReplayMemory import ReplaySampleSerializer
from Gomoku.Agent.ReplayMemory.ReplayMemory import ReplayMemory
from Gomoku.Agent.ReplayMemory.ReplayMemoryPersister import ReplayMemoryPersister


class ReplayMemoryManager:
    def __init__(self, persister: ReplayMemoryPersister, sample_serializer: ReplaySampleSerializer):
        self.persister = persister
        self.sample_serializer = sample_serializer
        self.managed_memories = {}

    def save(self, replay_memory: ReplayMemory, name: str = None) -> str:
        samples = []

        for i, sample in replay_memory.enumerate():
            samples.append(self.sample_serializer.serialize(sample))

        self.persister.save(samples, name)

    def load(self, name: str) -> ReplayMemory:
        samples = self.persister.load(name)
        memory = ReplayMemory()

        for _, sample_raw in enumerate(samples):
            sample = self.sample_serializer.deserialize(sample_raw)
            memory.add_sample(sample)

        return memory

    def unique(self, memory: ReplayMemory) -> ReplayMemory:
        unique_items = {}

        for i, sample in memory.enumerate():
            serialized_sample = self.sample_serializer.serialize(sample)
            key = base64.encodebytes(serialized_sample)
            unique_items[key] = sample

        def enum_dict_values(dict):
            for i, v in enumerate(dict.values()):
                yield v

        result = ReplayMemory()
        result.add_samples(enum_dict_values(unique_items))

        return result