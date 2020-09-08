"""
3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""
flag = True
while flag:
    n = input("Введите число n:\n")
    if n.isdigit():
        flag = False
        n = int(n)
Sum = 100 * n + 20 * n + 3 * n   # n + nn + nnn = n + (10 * n + n) + (100 * n + 10 * n + n) = 100 * n + 20 * n + 3 * n
print(f"Сумма чисел n + nn + nnn = {Sum}")


