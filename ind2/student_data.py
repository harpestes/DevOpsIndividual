from ind2.desired_performance import DesiredPerformance
from ind2.real_performance import RealPerformance
from ind2.student import Student


class StudentData:
    def __init__(self, student: Student, real_performance: RealPerformance, desired_performance: DesiredPerformance):
        self.__student = student
        self.__real_performance = real_performance
        self.__desired_performance = desired_performance

    def to_dictionary(self) -> dict:
        return {
            "student": {
                "full_name": self.__student.get_full_name(),
                "group": self.__student.get_group(),
                "date_of_birth": self.__student.get_date_of_birth().isoformat(),
            },
            "real_performance": {
                "subjects": self.__real_performance.get_subjects(),
                "grades": self.__real_performance.get_grades(),
                "average_grade": self.__real_performance.average_grade()
            },
            "desired_performance": {
                "subjects": self.__desired_performance.get_subjects(),
                "grades": self.__desired_performance.get_grades(),
                "average_grade": self.__desired_performance.average_grade()
            }
        }