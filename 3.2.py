"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_info_input(first_name, last_name, birth_year, city, email, phone_number):
    print(f"Имя: {first_name}, Фамилия: {last_name}, Год рождения: {birth_year}, Город проживания: {city}, Почта: {email}, Номер телефона: {phone_number}")


user_info_input(last_name="Shibanov", first_name="Aleksandr", email="qwerty@gmail.com", phone_number="+1234567890", birth_year="2001", city="Moscow")