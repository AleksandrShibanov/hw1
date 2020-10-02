"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. 
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, 
а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""
from abc import ABC, abstractmethod


class OwnException(Exception):
    def __init__(self, txt):
        self.txt = txt


class Storage:
    __storage_products = {}
    __storage_products_count = {}

    @staticmethod
    def control(some):
        try:
            if not (isinstance(some.id, str) and isinstance(some.name, str) and isinstance(some.e_type, str)):
                raise OwnException("Неправильно введены общие данные товара")
            elif isinstance(some, Printer) and not(isinstance(some.ammount_of_paper, int)
                                                 and isinstance(some.colored, bool)
                                                 and isinstance(some.printer_type, str)):
                raise OwnException("Неправильно введены данные для принтера")
            elif isinstance(some, Scaner) and not (isinstance(some.sensor, str)
                                                 and isinstance(some.resolution, int)
                                                 and isinstance(some.color_per_bit, int)):
                raise OwnException("Неправильно введены данные для сканера")
            elif isinstance(some, Xerox) and not (isinstance(some.paper_A_size, int)
                                                 and isinstance(some.resolution, int)):
                raise OwnException("Неправильно введены данные для ксерокса")
        except OwnException as e:
            print(e, "\nАварийное завершение программы...")
            quit()

    def add_to_storage(self, some):
        if some.e_type in self.__storage_products:
            self.__storage_products[some.e_type].append(some)
        else:
            self.__storage_products[some.e_type] = [some]

    def add_to_count(self, some):
        if some.e_type in self.__storage_products_count:
            self.__storage_products_count[some.e_type] += 1
        else:
            self.__storage_products_count[some.e_type] = 1


class Equipment(ABC):
    id = ""
    name = ""
    e_type = ""

    @abstractmethod
    def add_equipment(self, some_storage):
        pass


class Printer(Equipment):
    ammount_of_paper = 0
    colored = False
    printer_type = ""

    def __init__(self, id, name, ammount_of_paper, colored, printer_type):
        super().__init__(id, name, type(Printer))
        self.ammount_of_paper = ammount_of_paper
        self.colored = colored
        self.printer_type = printer_type

    def add_equipment(self, some_storage: Storage):
        Storage.control(self)
        some_storage.add_to_storage(self)
        some_storage.add_to_count(self)


class Scaner(Equipment):
    sensor = ""
    resolution = 0
    color_per_bit = 0

    def __init__(self, id, name, sensor, resolution, color_per_bit):
        super().__init__(id, name, type(Scaner))
        self.sensor = sensor
        self.resolution = resolution
        self.color_per_bit = color_per_bit

    def add_equipment(self, some_storage: Storage):
        Storage.control(self)
        some_storage.add_to_storage(self)
        some_storage.add_to_count(self)


class Xerox(Equipment):
    paper_A_size = 0
    resolution = 0

    def __init__(self, id, name, paper_A_size, resolution):
        super().__init__(id, name, type(Xerox))
        self.resolution = resolution
        self.paper_A_size = paper_A_size

    def add_equipment(self, some_storage: Storage):
        Storage.control(self)
        some_storage.add_to_storage(self)
        some_storage.add_to_count(self)

