import csv

from ind2.data_saver import DataSaver


class CSVSaver(DataSaver):
    def save(self, data_list: list[dict], filename: str):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            for student_number, data in enumerate(data_list, start=1):
                writer.writerow([f"Student #{student_number}"])
                writer.writerow(["Full Name", "Group", "Birth Date"])
                s = data["student"]
                writer.writerow([s["full_name"], s["group"], s["date_of_birth"]])

                writer.writerow([])
                writer.writerow(["Subject", "Grade"])
                for subject, grade in zip(data["real_performance"]["subjects"], data["real_performance"]["grades"]):
                    writer.writerow([subject, grade])
                writer.writerow(["Average", data["real_performance"]["average_grade"]])

                writer.writerow([])
                writer.writerow(["Subject", "Desired Grade"])
                for subject, grade in zip(data["desired_performance"]["subjects"], data["desired_performance"]["grades"]):
                    writer.writerow([subject, grade])
                writer.writerow(["Desired Average", data["desired_performance"]["average_grade"]])

                writer.writerow([])