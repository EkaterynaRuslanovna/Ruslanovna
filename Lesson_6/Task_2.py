from math import sqrt

# 2. Напишіть функцію square, яка приймає 1 аргумент, сторону квадрата, і повертає 3 значення (за допомогою кортежу):
# периметр квадрата, площа квадрата та діагональ квадрата.


def square(side_of_the_square):
    try:
        if side_of_the_square > 0:
            p = side_of_the_square * 4
            s = side_of_the_square ** 2
            d = side_of_the_square * sqrt(2)
            print(f"Периметр квадрату = {p}, \nПлоща квадрату = {s}, \nДіагональ квадрату = {d}")
            return p, s, d
        else:
            print("ERROR: Сторона квадрату не може бути менше або дорівнювати 0")
    except TypeError:
        print("ERROR: Функція приймає лише числові значення")