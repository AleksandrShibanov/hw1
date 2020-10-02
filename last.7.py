"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""

class Complex:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex(self.x+other.x, self.y+other.y)

    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)

    def __str__(self):
        return f"{self.x} + {self.y}i"


z1 = Complex(3, 5)
z2 = Complex(2, 5)
z3 = Complex(0, -3)
print(z1+z2)
print(z1*z2)
print(z1+z3)
print(z1*z3)
