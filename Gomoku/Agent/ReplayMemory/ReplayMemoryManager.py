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
            memory.add_sample(sample.state, sample.action, sample.reward, sample.next_state, sample.done)

        return memory

    def sync(self, replay_memory: ReplayMemory, name: str = None) -> str:
        """
        Saves replay memory to a named slot and fetches new entries which could
        have appeared from parallel processes.
        """
        pass