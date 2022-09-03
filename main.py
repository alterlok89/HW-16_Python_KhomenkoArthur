import math

# Задание 1 - 2

print('Задание 1 и 2\n')


class Figure:
    def __init__(self, name: str):
        self.name = name

    def get_area(self):
        return 0

    def __str__(self):
        return f'Фигура: {self.name}\n' \
               f'Площадь: {self.get_area()}\n'


print(Figure)


# Прямоугольник
class Rectangle(Figure):
    # функция принимает длину и ширину
    def __init__(self, a: int, b: int):
        self.a, self.b = a, b
        # передаем в родительский класс название фигуры
        super().__init__('Прямоугольник')

    def get_area(self):
        return self.a * self.b


print(Rectangle(20, 10))


# Круг
class Circle(Figure):
    # функция принимает радиус
    def __init__(self, radius: float):
        self.radius = radius
        super().__init__('Круг')

    def get_area(self):
        pi = round(float(math.pi), 4)
        return round((pi * (self.radius ** 2)), 2)


print(Circle(10))


# Прямоугольный треугольник
class RightTriangle(Figure):
    # функция принимает длины катетов
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        super().__init__('Прямоугольный треугольник')

    def get_area(self):
        return self.a * self.b / 2


print(RightTriangle(20, 10))

# Трапеция
class Trapezoid(Figure):
    # функция принимает длины нижнего, верхнего оснований и высоту трапеции
    def __init__(self, a: int, b: int, h: int):
        self.a = a
        self.b = b
        self.h = h
        super().__init__('Трапеция')

    def get_area(self):
        return ((self.a + self.b) / 2) * self.h


print(Trapezoid(10, 20, 5))


