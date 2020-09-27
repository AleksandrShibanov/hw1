"""
3. Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
"""


class Worker:

    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        total = 0
        for value in self._income.values():
            total += value
        return total


res1 = Position('Egor', 'Egorov', 'Director', 500000, 0)
res2 = Position('Ivan', 'Ivanov', 'Operator', 150000, 50000)
print(res1.get_full_name())
print(res1.position)
print(res1.get_total_income())
print("*" * 20)
print(res2.get_full_name())
print(res2.position)
print(res2.get_total_income())
