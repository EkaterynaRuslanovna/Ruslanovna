"""

2. Напишіть функцію square, яка приймає 1 аргумент, сторону квадрата, і повертає 3 значення (за допомогою кортежу):
периметр квадрата, площа квадрата та діагональ квадрата.

"""
from math import sqrt


def square(side_of_the_square: float) -> tuple:
    try:
        if side_of_the_square > 0:
            p = side_of_the_square * 4
            s = side_of_the_square ** 2
            d = side_of_the_square * sqrt(2)
            return p, s, d
        else:
            print(f"ERROR! Сторона квадрату не може бути менше або дорівнювати 0, ви ввели {side_of_the_square}")
    except TypeError:
        print(f"ERROR! Функція square приймає лише значення типу int, float, ви ввели {type(side_of_the_square)}")