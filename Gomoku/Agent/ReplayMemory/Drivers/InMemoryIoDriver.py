import io

from Gomoku.Agent.ReplayMemory.Contracts.IoDriverInterface import IoDriverInterface


class InMemoryIoDriver(IoDriverInterface):
    def __init__(self):
        self.opened_files = {}

    def open(self, name: str, mode: str):
        if name not in self.opened_files:
            file = io.BytesIO()
            file.close = lambda: None
            self.opened_files[name] = file

        if mode[0] == "r":
            file = io.BytesIO(self.opened_files[name].getvalue())
        else:
            file = self.opened_files[name]

        return file
