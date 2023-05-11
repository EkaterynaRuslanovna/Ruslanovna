# Написать класс для сущности Точка(содержит в себе координаты Х и Y).
# Написать классы для сущностей Треугольник, Квадрат, которые агрегируют объекты класса Точка.
# Написать методы, которые считают площадь фигур, если координаты введены правильно.
# Если нет, то показать сообщение об ошибке.

"""
Длина стороны: a = ((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2) ** 0.5
Площадь треугольника: S = sqrt(p * (p - a) * (p - b) * (p - c))
Периметр треугольника: p = (a + b + c) / 2
Площадь квадрата: S = a**2
"""


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, point_1: Point, point_2: Point, point_3: Point):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    def area(self):
        a = ((self.point_1.x - self.point_2.x) ** 2 + (self.point_1.y - self.point_2.y) ** 2) ** 0.5
        b = ((self.point_2.x - self.point_3.x) ** 2 + (self.point_2.y - self.point_3.y) ** 2) ** 0.5
        c = ((self.point_3.x - self.point_1.x) ** 2 + (self.point_3.y - self.point_1.y) ** 2) ** 0.5
        if a + b > c and b + c > a and c + a > b:
            p = (a + b + c) / 2
            return (p * (p - a) * (p - b) * (p - c)) ** 0.5
        else:
            raise ValueError("Error: невірні координати трикутника")


class Square:
    def __init__(self, point_1: Point, point_2: Point, point_3: Point, point_4: Point):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        self.point_4 = point_4

    def area(self):
        a = ((self.point_1.x - self.point_2.x) ** 2 + (self.point_1.y - self.point_2.y) ** 2) ** 0.5
        b = ((self.point_2.x - self.point_3.x) ** 2 + (self.point_2.y - self.point_3.y) ** 2) ** 0.5
        c = ((self.point_3.x - self.point_4.x) ** 2 + (self.point_3.y - self.point_4.y) ** 2) ** 0.5
        d = ((self.point_4.x - self.point_1.x) ** 2 + (self.point_4.y - self.point_1.y) ** 2) ** 0.5
        if a == b and b == c and c == d:
            return a ** 2
        else:
            raise ValueError("Error: невірні координати квадрата")