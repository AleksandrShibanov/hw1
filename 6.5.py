"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки”.
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = ""

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисует {self.title} ручка")


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисует {self.title} карандаш")


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисует {self.title} маркер")


pen = Pen("синяя, шариковая")
pencil = Pencil("тонкий")
handle = Handle("красный")
pen.draw()
pencil.draw()
handle.draw()
