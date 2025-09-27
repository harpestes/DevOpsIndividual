from abc import ABC, abstractmethod
from typing import List

from ind2.student_data import StudentData


class DataSaver(ABC):
    @abstractmethod
    def save(self, data_list: List[StudentData], filename: str):
        pass