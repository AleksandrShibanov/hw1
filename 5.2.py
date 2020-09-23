"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
try:
    with open("5_2_text.txt", "r", encoding="UTF-8") as r_file:
        counter = 0
        for line in r_file:
            counter += 1
            print(f"Количество слов в {counter} - ой строке: {len(line.split())}")
        print(f"Количество строк: {counter}")
except FileNotFoundError or FileExistsError:
    print("Файла не существует...")
