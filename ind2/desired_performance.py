from typing import List
from ind2.performance import Performance


class DesiredPerformance(Performance):
    def __init__(self, subjects: List[str], desired_grades: List[int]):
        super().__init__(subjects, desired_grades)

    def average_grade(self) -> float:
        grades = super().get_grades()
        if not grades:
            return 0
        return sum(grades) / len(grades)