"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(*args):
    my_list = list(args)
    first_max = max(my_list)
    my_list.remove(max(my_list))
    return first_max + max(my_list)


first = input("Введите первое число:\n")
second = input("Введите второе число:\n")
third = input("Введите третье число:\n")
try:
    print(f"Сумма наибольших двух аргументов: {my_func(float(first), float(second), float(third))}")
except ValueError:
    print("Вы ввели не числа!")