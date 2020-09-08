"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
flag = True
while flag:
    time = (input("Введите время в секундах:\n"))
    if time.isdigit():
        flag = False
        time = int(time)
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - hours * 3600 - minutes * 60
if hours < 10:
    hours = '0' + str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
if seconds < 10:
    seconds = '0' + str(seconds)
print(f"Время в формате чч:мм:cc = {hours}:{minutes}:{seconds}")