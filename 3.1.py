"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def divide(x, y):
    try:
        print(f"Результат деления первого числа на второе: {float(x)/float(y)}")
        return float(x)/float(y)
    except ValueError:
        print("Введены не числа!")
    except ZeroDivisionError:
        print("Нельзя делить на ноль!")


first = input("Введите первое число:\n")
second = input("Введите второе число:\n")
divide(first, second)
