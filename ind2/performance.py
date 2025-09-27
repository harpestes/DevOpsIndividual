from abc import ABC, abstractmethod
from typing import List


class Performance(ABC):
    def __init__(self, subjects: List[str], grades: List[int]):
        self.__subjects = subjects
        self.__grades = grades

    @abstractmethod
    def average_grade(self) -> float:
        pass

    def get_subjects(self) -> List[str]:
        return self.__subjects

    def get_grades(self) -> List[int]:
        return self.__grades