from ind2.saver.data_saver import DataSaver
from xml.etree import ElementTree

class XMLSaver(DataSaver):
    def save(self, data_list: list[dict], filename: str):
        root = ElementTree.Element("Students")

        for data in data_list:
            student_elem = ElementTree.SubElement(root, "StudentData")

            stud = ElementTree.SubElement(student_elem, "Student")
            for key, value in data["student"].items():
                ElementTree.SubElement(stud, key).text = str(value)

            real_perf = ElementTree.SubElement(student_elem, "RealPerformance")
            for key, value in data["real_performance"].items():
                ElementTree.SubElement(real_perf, key).text = str(value)

            desired_perf = ElementTree.SubElement(student_elem, "DesiredPerformance")
            for key, value in data["desired_performance"].items():
                ElementTree.SubElement(desired_perf, key).text = str(value)

        tree = ElementTree.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)