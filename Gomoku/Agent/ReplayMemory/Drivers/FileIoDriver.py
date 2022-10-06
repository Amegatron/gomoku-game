from Gomoku.Agent.ReplayMemory.Contracts.IoDriverInterface import IoDriverInterface


class FileIoDriver(IoDriverInterface):
    def __init__(self, working_dir: str):
        self.working_dir = working_dir

    def open(self, name: str, mode: str):
        return open(self.working_dir + '/' + name + '.mem', mode)