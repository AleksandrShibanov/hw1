"""
1. Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.
"""

first_int = 5
first_int *= 3
first_str = "first"
second_str = 'second'
print(first_int)
print(first_str + " and " + second_str)
print(first_int * second_str)

print(first_str < second_str)


first_input = input("Введите числа, которые хотите перемножить:\n")
second_input = input()
if first_input.isdigit() and second_input.isdigit():
    print(f"Ответ: { float(first_input) * float(second_input) }")
else:
    print("Вы ввели не числа, в таком случае программа не может их перемножить.")

first_input = input("Введите строки, которые хотите 'склеить' :\n")
second_input = input()
print(f"Ответ: {first_input + second_input}")




