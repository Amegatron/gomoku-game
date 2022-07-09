from Gomoku.Agent.ReplayMemory import ReplayMemoryPersister
from Gomoku.Agent.ReplayMemory.ReplayMemory import ReplayMemory


class ReplayMemoryManager:
    def __init__(self, persister: ReplayMemoryPersister):
        self.persister = persister
        self.managed_memories = {}

    def save(self, replay_memory: ReplayMemory, name: str = None) -> str:
        """
            Saves replay memory to a named slot. If that slot does not exist yet,
            it will be created. If it already exists, saving will ADD memory to
            that slot.
        """
        pass

    def load(self, name: str) -> ReplayMemory:
        """
            Loads replay memory from named slot, returning new instance or ReplayMemory.
            If such slot does not exist, error will be raised.
        """
        pass

    def sync(self, replay_memory: ReplayMemory, name: str = None) -> str:
        """
            Saves replay memory to a names slot and fetches new entries which could
            have appeared from parallel processes.
        """
        pass