"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""


def my_func(x, y):
    if y >= 0:
        return print("Ошибка ввода!")
    try:
        1/x
    except ZeroDivisionError:
        print("Нельзя делить на ноль!")
        quit()
    res = 1
    for i in range(0, y, -1):
        res *= 1/x
    return res


first = input("Введите первое число:\n")
second = input("Введите второе число:\n")
try:
    print(f"Результат возведения числа {first} в степень {second} = %.2f" % my_func(float(first), int(second)))
except ValueError:
    print("Ошибка ввода!")
