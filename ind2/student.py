from datetime import date


class Student:
    def __init__(self, full_name: str, group_name: str, date_of_birth: date):
        self.__full_name = full_name
        self.__group_name = group_name
        self.__date_of_birth = date_of_birth

    def get_full_name(self) -> str:
        return self.__full_name

    def get_group(self) -> str:
        return self.__group_name

    def get_date_of_birth(self) -> date:
        return self.__date_of_birth

    def set_full_name(self, full_name: str):
        self.__full_name = full_name

    def set_group(self, group_name: str):
        self.__group_name = group_name

    def set_birth_date(self, date_of_birth: date):
        self.__date_of_birth = date_of_birth