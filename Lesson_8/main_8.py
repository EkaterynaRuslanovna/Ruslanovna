from Task_1 import ComplexNumber
from Task_2 import Point
from Task_2 import Triangle
from Task_2 import Square
from Task_3_Class_Record import Record
from Task_3_Class_PhoneBook import Phonebook
from Task_3_Class_Interface import Interface

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
