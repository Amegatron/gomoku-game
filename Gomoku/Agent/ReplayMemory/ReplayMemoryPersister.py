import glob
import os


class ReplayMemoryPersister:
    """
    Driver for persisting replay memory
    """
    def __init__(self, working_dir: str):
        self.working_dir = working_dir

    def load(self, slot_name: str):
        filename = self.__get_slot_filename(slot_name)
        result = []

        with open(filename, "rb") as file:
            while True:
                sample_len_raw = file.read(2)

                if not sample_len_raw:
                    break

                sample_len = int.from_bytes(sample_len_raw, "little")
                sample = file.read(sample_len)
                result.append(sample)

        return result

    def save(self, serialized_samples, slot_name: str):
        filename = self.__get_slot_filename(slot_name)

        with open(filename, "wb") as file:
            for _, sample in enumerate(serialized_samples):
                result = bytearray()
                result += len(sample).to_bytes(2, "little")
                result += sample
                file.write(result)

    def __get_slot_filename(self, slot_name: str):
        return self.working_dir + '/' + slot_name + '.mem'
