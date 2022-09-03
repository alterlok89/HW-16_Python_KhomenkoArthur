import math
import sys

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


# Задание 3

print('Задание 3', end='\n\n')


class Shape:
    def __init__(self, name: str):
        self.name = name

    def show(self):
        pass

    def save(self):
        pass

    def load(self):
        pass

    def __str__(self):
        return f'{self.name}'


class Square(Shape):
    # координата x и y верхнего левого угла, length - длина стороны
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length
        super().__init__('Квадрат')

    def show(self):
        self.show = f'Фигура: {super().__str__()} --> ' \
                           f'Координата верхенего левого угла (x, y): ({self.x}, {self.y}) - ' \
                           f'Длина стороны: {self.length}'
        # print(self.show)
        return self.show

    def save(self):
        with open('Shape.txt', 'a', encoding='utf-8') as file:
             file.write(f'{self.show()}\n')

    def load(self):
        with open('Shape.txt', 'r', encoding='utf-8') as file:
             text = file.read()
        return text


print(Square(5, 10, 3).show())
Square(5, 10, 3).save()
Square(10, 15, 4).save()
Square(-5, 5, 6).save()
text = Square(-5, 5, 6).load()
print(text)


class Rectangle(Shape):
    # координата x и y верхнего левого угла, a - длина, b - ширина
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        super().__init__('Прямоугольник')

    def show(self):
        self.show = f'Фигура: {super().__str__()} --> ' \
                           f'Координата верхенего левого угла (x, y): ({self.x}, {self.y}) - ' \
                           f'Длина: {self.a} - Ширина: {self.b}'
        # print(self.show)
        return self.show

    def save(self):
        with open('Shape.txt', 'a', encoding='utf-8') as file:
             file.write(f'{self.show()}\n')

    def load(self):
        with open('Shape.txt', 'r', encoding='utf-8') as file:
             text = file.read()
        return text


print(Rectangle(5, 10, 3, 6).show())
Rectangle(5, 10, 3, 3).save()
Rectangle(10, 15, 4, 10).save()
Rectangle(-5, 5, 6, 15).save()
text = Rectangle(-5, 5, 6, 15).load()
print(text)


class Circle(Shape):
    # координата x и y центра круга, rad - радиус
    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.rad = rad
        super().__init__('Круг')

    def show(self):
        self.show = f'Фигура: {super().__str__()} --> ' \
                           f'Координата центра (x, y): ({self.x}, {self.y}) - ' \
                           f'Длина стороны: {self.rad}'
        # print(self.show)
        return self.show

    def save(self):
        with open('Shape.txt', 'a', encoding='utf-8') as file:
             file.write(f'{self.show()}\n')

    def load(self):
        with open('Shape.txt', 'r', encoding='utf-8') as file:
             text = file.read()
        return text


print(Circle(5, 10, 3).show())
Circle(5, 10, 3).save()
Circle(10, 15, 4).save()
Circle(-5, 5, 6).save()
text = Circle(-5, 5, 6).load()
print(text)


class Ellipse(Shape):
    # координата x и y верхнего левого угла прямоугольника в который вписан элипс
    # a - длина, b - ширина этого прямоугольника
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        super().__init__('Эллипс')

    def show(self):
        self.show = f'Фигура: {super().__str__()} --> ' \
                           f'Координата верхенего левого угла (x, y): ({self.x}, {self.y}) - ' \
                           f'Длина: {self.a} - Ширина: {self.b}'
        # print(self.show)
        return self.show

    def save(self):
        with open('Shape.txt', 'a', encoding='utf-8') as file:
             file.write(f'{self.show()}\n')

    def load(self):
        with open('Shape.txt', 'r', encoding='utf-8') as file:
             text = file.read()
        return text


print(Ellipse(5, 10, 3, 6).show())
Ellipse(5, 10, 3, 3).save()
Ellipse(10, 15, 4, 10).save()
Ellipse(-5, 5, 6, 15).save()
text = Ellipse(-5, 5, 6, 15).load()
print(text)

# Список всех данных в файле
lines = [line for line in open('Shape.txt', 'r', encoding='utf-8')]
# Список всех данных о квадратах
lines_square = [line for line in open('Shape.txt', 'r', encoding='utf-8') if line.find('Квадрат') != -1]
# Список всех данных о прямоугольниках
line_rectangle = [line for line in open('Shape.txt', 'r', encoding='utf-8') if line.find('Прямоугольник') != -1]
# Список всех данных о кругах
line_circle = [line for line in open('Shape.txt', 'r', encoding='utf-8') if line.find('Круг') != -1]
# Список всех данных об эллипсах
line_ellipse = [line for line in open('Shape.txt', 'r', encoding='utf-8') if line.find('Эллипс') != -1]
print(f'Список всех данных в файле:\n'
      f'{lines}\n\n'
      f'Список всех данных о квадратах:\n'
      f'{lines_square}\n\n'
      f'Список всех данных о прямоугольниках:'
      f'{line_rectangle}\n\n'
      f'Список всех данных о кругах:\n'
      f'{line_circle}\n\n'
      f'Список всех данных об эллипсах:\n'
      f'{line_ellipse}')


