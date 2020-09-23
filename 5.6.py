"""
6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и
общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def sum_of_lessons(lesson_str):
    numbers_list = lesson_str.split()
    i = 0
    while i < len(numbers_list):
        if not numbers_list[i] in {'-', '—'}:
            numbers_list[i] = int(numbers_list[i][:numbers_list[i].index("("):])
            i += 1
        else:
            numbers_list.remove(numbers_list[i])
    return sum(numbers_list)


lessons_dict = {}
try:
    with open("5_6_text.txt", "r", encoding="UTF-8") as r_file:
        try:
            for line in r_file:
                lessons_dict[line[:line.index(' ')-1:]] = sum_of_lessons(line[line.index(' ')+1::])
        except ValueError:
            print("Ошибка в текстовом файле!")
            quit()
    print(lessons_dict)
except FileNotFoundError or FileExistsError:
    print("Файла не существует...")
