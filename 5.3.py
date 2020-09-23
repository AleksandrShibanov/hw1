"""
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
try:
    with open("5_3_text.txt", "r", encoding="UTF-8") as r_file:
        counter = 0
        sum_of_money = 0
        for line in r_file:
            try:
                sum_of_money += float(line.split()[1])
                counter += 1
                if float(line.split()[1]) < 20000:
                    print(f"Сотрудник {line.split()[0]} имеет оклад менее 20 тыс.")
            except ValueError:
                print("\nВ файле нарушена последовательность данных")
                quit()
        try:
            print(f"\nСредняя величина дохода сотрудников: {sum_of_money/counter}")
        except ZeroDivisionError:
            print("\nПроизошло деление на ноль!")
            quit()
except FileNotFoundError or FileExistsError:
    print("Файла не существует...")
