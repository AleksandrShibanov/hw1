"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
my_str = ""
try:
    with open("5_4_text.txt", "r", encoding="UTF-8") as r_file:
        for line in r_file:
            my_str += my_dict.get(line.split()[0]) + " — " + line.split()[2] + '\n'
    with open("5_4_text_new.txt", "w", encoding="UTF-8") as w_file:
        w_file.write(my_str)
except FileNotFoundError or FileExistsError:
    print("Файла не существует...")
