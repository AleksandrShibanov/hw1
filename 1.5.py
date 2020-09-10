"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
proceeds = float(input("Введите значения выручки и издержек фирмы:\n"))
costs = float(input())
if proceeds > costs:
    print("Фирма приносит прибыль.\n")
    profitability = (proceeds - costs) / proceeds
    print(f"Рентабельность выручки: {profitability}\n")
    while True:
        num_of_employees = input("Введите число сотрудников фирмы:\n")
        if num_of_employees.isdigit():
            num_of_employees = int(num_of_employees)
            break
    profit_per_num = (proceeds - costs) / num_of_employees
    print(f"Прибыль фирмы в расчете на одного сотрудника: {profit_per_num}")
elif costs > proceeds:
    print("Фирма приносит убытки.")
elif costs == proceeds:
    print("Фирма не приносит ни убытков, ни выручки")
else:
    print("Ошибка!\n")