from Gomoku.Agent.ReplayMemory.Contracts.IoDriverInterface import IoDriverInterface


class ReplayMemoryPersister:
    """
    Driver for persisting replay memory
    """
    def __init__(self, io_driver: IoDriverInterface):
        self.io_driver = io_driver

    def load(self, slot_name: str):
        result = []

        with self.io_driver.open(slot_name, "rb") as file:
            while True:
                sample_len_raw = file.read(2)

                if not sample_len_raw:
                    break

                sample_len = int.from_bytes(sample_len_raw, "little")
                sample = file.read(sample_len)
                result.append(sample)

        return result

    def save(self, serialized_samples, slot_name: str):
        with self.io_driver.open(slot_name, "wb") as file:
            for _, sample in enumerate(serialized_samples):
                result = bytearray()
                result += len(sample).to_bytes(2, "little")
                result += sample
                file.write(result)
