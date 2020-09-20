"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл. Во втором также
необходимо предусмотреть условие, при котором повторение
элементов списка будет прекращено.
"""
from itertools import count, cycle


def a(condition_func, first):
    for i in count(first):
        if condition_func(i):
            yield i
        else:
            break


def b(k, some_list):
    counter = 0
    for i, val in cycle(enumerate(some_list)):
        counter += 1
        if counter / len(some_list) > k:
            break
        else:
            yield val


my_list = [23, 1, 3, 10, 4, 11]
print(list(a(lambda x: x < 11, 3)))
print(list(b(3, my_list)))
