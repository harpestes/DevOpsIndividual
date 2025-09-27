from datetime import date

from ind2.desired_performance import DesiredPerformance
from ind2.real_performance import RealPerformance
from ind2.saver.csv_saver import CSVSaver
from ind2.saver.json_saver import JsonSaver
from ind2.saver.xml_saver import XMLSaver
from ind2.student import Student
from ind2.student_data import StudentData

BASE_PATH = "Dykalo_PDM51_IND2"

student = Student("Попінако Єгор Олексійович", "ПДМ-51", date(2004, 5, 12))
real_perf = RealPerformance(["КДС", "ОБДЗ"], [85, 90])
desired_perf = DesiredPerformance(["КДС", "ОБДЗ"], [95, 100])
data = StudentData(student, real_perf, desired_perf)

student1 = Student("Дикало Андрій Юрійович", "ПДМ-51", date(2004, 10, 17))
real_perf1 = RealPerformance(["КДС", "ОБДЗ"], [90, 90])
desired_perf1 = DesiredPerformance(["КДС", "ОБДЗ"], [98, 100])
data1 = StudentData(student1, real_perf1, desired_perf1)

students_data = [
    data.to_dictionary(),
    data1.to_dictionary(),
]

JsonSaver().save(students_data, BASE_PATH + ".json")
XMLSaver().save(students_data, BASE_PATH + ".xml")
CSVSaver().save(students_data, BASE_PATH + ".csv")
