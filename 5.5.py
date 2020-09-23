"""
5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
try:
    with open("5_5_text.txt", "w", encoding="UTF-8") as w_file:
        for i in range(101):
            w_file.write(str(i) + ' ')
    with open("5_5_text.txt", "r", encoding="UTF-8") as r_file:
        print(f"Сумма чисел в файле: {sum(map(lambda x: int(x), r_file.read().split()))}")
except ValueError or FileNotFoundError or FileExistsError:
    print("Ошибка!")
