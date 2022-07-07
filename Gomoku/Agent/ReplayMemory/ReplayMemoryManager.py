from Gomoku.Agent.ReplayMemory.ReplayMemory import ReplayMemory


class ReplayMemoryManager:
    def __init__(self):
        pass

    def save(self, replay_memory: ReplayMemory, name: str = None) -> str:
        pass

    def load(self, name: str) -> ReplayMemory:
        pass

    def sync(self, replay_memory: ReplayMemory, name: str = None) -> str:
        pass