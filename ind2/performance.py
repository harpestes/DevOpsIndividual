from abc import ABC, abstractmethod
from typing import List


class Performance(ABC):
    def __init__(self, subjects: List[str], grades: List[int]):
        self.__subjects = subjects
        self.__grades = grades

    @abstractmethod
    def average_grade(self) -> float:
        pass