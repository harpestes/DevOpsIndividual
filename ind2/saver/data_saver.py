from abc import ABC, abstractmethod
from typing import List


class DataSaver(ABC):
    @abstractmethod
    def save(self, data_list: List[dict], filename: str):
        pass