from abc import ABC, abstractmethod


class DataSaver(ABC):
    @abstractmethod
    def save(self, data_list: list[dict], filename: str):
        pass