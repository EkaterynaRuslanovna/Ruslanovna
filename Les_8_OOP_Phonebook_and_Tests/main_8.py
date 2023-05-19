from complex_number import ComplexNumber
from classes_point_triangle_square import Point
from classes_point_triangle_square import Triangle
from classes_point_triangle_square import Square
from class_record import Record
from class_phoneBook import Phonebook
from class_interface import Interface

if __name__ == '__main__':
    print("---------------------------------------------Завдання 1---------------------------------------------")

    try:
        a = ComplexNumber(2, -8)
        b = ComplexNumber(1, -1)
        c = ComplexNumber(4, -3)

        print(a, b + c, b - c, b == c, b != c, sep="\n")
    except TypeError as error:
        print(error)
    except AttributeError as error:
        print(error)

    print("---------------------------------------------Завдання 2---------------------------------------------")

    try:

        a = Point(-2, 8)
        b = Point(6, -2)
        c = Point(-2, -12)
        d = Point(5, 3)

        e = Triangle(a, b, c)
        print(e.area())

        f = Square(a, b, a, b)
        print(f.area())

    except TypeError as error:
        print(error)
    except ValueError as error:
        print(error)

    print("---------------------------------------------Завдання 3---------------------------------------------")

    try:
        book = Phonebook()
        book.view_all_records()

        print("------------------------------------------------------------------------------------------")

        user = Record(name="Kate", mobile_phone="8768768765", surname="Ruslanovna", birthday="30.05.94")
        book.add_record(user)
        book.view_all_records()

        print("------------------------------------------------------------------------------------------")

        interface = Interface(book)
        interface.run()
    except Exception as error:
        print(error)
