"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class OwnZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    a, b = input("Введите два числа:\n"), input()
    try:
        if float(b) == 0:
            raise OwnZeroError("Деление на ноль!")
        else:
            print(f"Результат деления первого числа на второе: {float(a)/float(b)}")
            break
    except OwnZeroError as err:
        print(err)
    except ValueError as err:
        print(err)
