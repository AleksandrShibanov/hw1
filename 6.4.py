"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости.
"""


class Car:

    speed = 0
    color = ""
    name = ""
    is_police = ""

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Машина {self.name} поехала"

    def stop(self):
        return f"Машина {self.name} остановилась"

    def turn(self, direction):
        return f"Машина {self.name} повернула {direction}"

    def show_speed(self):
        return self.speed


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return "Вы превысили скорость!"
        else:
            return "Скорость не превышена"


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return "Вы превысили скорость!"
        else:
            return "Скорость не превышена"


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


sport_car = SportCar(180, 'Черный', 'Porsche', False)
town_car = TownCar(30, 'Белый', 'Mazda', False)
work_car = WorkCar(60, 'Синий', 'Nissan', True)
police_car = PoliceCar(100, 'Черный',  'Ford', True)


print(police_car.turn("направо"))
print(f'После того как {town_car.turn("налево")}, {sport_car.stop()}')
print(f'{police_car.go()} со скоростью {police_car.show_speed()}')
print(f'{police_car.name} цвета {police_car.color}')
print(f'{sport_car.name} - полицейская машина? {sport_car.is_police}')
print(f'{police_car.name} - полицейская машина? {police_car.is_police}')
print(sport_car.show_speed())
print(town_car.show_speed())
