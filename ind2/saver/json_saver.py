import json
from typing import List

from ind2.saver.data_saver import DataSaver


class JsonSaver(DataSaver):
    def save(self, data_list: List[dict], filename: str):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data_list, file, ensure_ascii=False, indent=4)