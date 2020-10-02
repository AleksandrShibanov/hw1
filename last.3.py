"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


ls = []
while (a := input("Введите число. Для прекращения ввода - stop\n")) != "stop":
    try:
        if not a.isdigit() and not isfloat(a):
            raise OwnError("Введено не число!")
        ls.append(float(a))
    except OwnError as e:
        print(e)
print(ls)
