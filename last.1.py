"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class OwnException(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date:

    def __init__(self, date_list):
        self.__day = date_list[0]
        self.__month = date_list[1]
        self.__year = date_list[2]

    @classmethod
    def converting(cls, date_str):
        date_list = [int(itm) for itm in date_str.split('-')]
        return cls(date_list)

    @staticmethod
    def control(date_str):
        date_list = [int(itm) for itm in date_str.split('-')]
        try:
            if date_list[0] // 32 != 0 or date_list[0] == 0:
                raise OwnException("День указан неправильно")
            if date_list[1] // 13 != 0 or date_list[1] == 0:
                raise OwnException("Месяц указан неправильно")
        except OwnException as err:
            print(err)
            quit()

    def __str__(self):
        return f"Дата: {self.__day}.{self.__month:02}.{self.__year}"


my_date = "25-05-2016"
Date.control(my_date)
print(Date.converting(my_date))
