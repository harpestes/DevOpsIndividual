from typing import List
from ind2.performance import Performance


class DesiredPerformance(Performance):
    def __init__(self, subjects: List[str], desired_grades: List[int]):
        super().__init__(subjects, desired_grades)

    def average_grade(self) -> float:
        if not self.__grades:
            return 0
        return sum(self.__grades) / len(self.__grades)