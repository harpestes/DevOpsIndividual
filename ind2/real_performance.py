from typing import List
from ind2.performance import Performance


class RealPerformance(Performance):
    def __init__(self, subjects: List[str], real_grades: List[int]):
        super().__init__(subjects, real_grades)

    def average_grade(self) -> float:
        grades = super().get_grades()
        if not grades:
            return 0
        return sum(grades) / len(grades)