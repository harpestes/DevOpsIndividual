from abc import ABC, abstractmethod


class Performance(ABC):
    def __init__(self, subjects: list[str], grades: list[int]):
        self.__subjects = subjects
        self.__grades = grades

    @abstractmethod
    def average_grade(self) -> float:
        pass

    def get_subjects(self) -> list[str]:
        return self.__subjects

    def get_grades(self) -> list[int]:
        return self.__grades