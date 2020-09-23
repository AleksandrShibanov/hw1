"""
7. Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки,
в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json


try:
    with open("5_7_text.txt", "r", encoding="UTF-8") as r_file:
        profit_dict = {}
        profit_sum = 0
        counter = 0
        try:
            for line in r_file:
                if float(line.split()[2]) - float(line.split()[3]) > 0:
                    profit_sum += float(line.split()[2]) - float(line.split()[3])
                    counter += 1
                profit_dict[line.split()[0]] = round(float(line.split()[2]) - float(line.split()[3]), 3)
        except ValueError:
            print("Ошибка в текстовом файле!")
            quit()
        try:
            average_profit = {"average_profit": round(profit_sum/counter, 3)}
        except ZeroDivisionError:
            print("Деление на ноль!")
            quit()
    with open("5_7_json.json", "w", encoding="UTF-8") as j_file:
        json.dump([profit_dict, average_profit], j_file)
except FileNotFoundError or FileExistsError:
    print("Файла не существует...")
