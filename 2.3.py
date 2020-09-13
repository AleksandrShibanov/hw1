"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
year_list = ["#",
             "зима", "зима",
             "весна", "весна", "весна",
             "лето", "лето", "лето",
             "осень", "осень", "осень",
             "зима"]
year_dict = {(12, 1, 2): "зима", (3, 4, 5): "весна", (6, 7, 8): "лето", (9, 10, 11): "осень"}
while True:
    int_month = input("Введите месяц в виде целого числа от 1 до 12\n")
    if int_month.isdigit() and 1 <= int(int_month) <= 12:
        int_month = int(int_month)
        break
    else:
        print("Ошибка ввода!")
print(f"Месяц относится к времени года: {year_list[int_month]}")
for T_int_months_of_season, season in year_dict.items():
    if int_month in T_int_months_of_season:
        print(f"Месяц относится к времени года: {season}")