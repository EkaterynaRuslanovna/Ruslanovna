# Реализовать так, чтоб если пользователь из клавиатуры вводит математический знак, то он не превращался в string
from re import search


def calculate(formula):
    try:
        if search(r'[0-9][()!@#$%^&_=|\\a-zA-Zа-яА-Я][0-9]', formula):
            raise SyntaxError(f"ERROR! Невірний операнд, ви ввели {formula}")
        elif search(r'[()!@#$%^&+\-/*_=|\\a-zA-Zа-яА-Я][+\-/*][()!@#$%^&_=|\\a-zA-Zа-яА-Я+\-/*]', formula):
            raise SyntaxError(f"ERROR! Невірно введені аргументи формули, ви ввели {formula}")
        elif search(r'[0-9][+\-/*][()!@#$%^&_=|\\a-zA-Zа-яА-Я+\-/*]', formula):
            raise SyntaxError(f"ERROR! Невірно введений другий аргумент формули, ви ввели {formula}")
        elif search(r'[()!@#$%^&_=|\\a-zA-Zа-яА-Я+\-/*][+\-/*][0-9]', formula):
            raise SyntaxError(f"ERROR! Невірно введений перший аргумент формули, ви ввели {formula}")
        elif search(r'[()!@#$%^&+\-/*_=|\\a-zA-Zа-яА-Я][()!@#$%^&+\-/*_=|\\a-zA-Zа-яА-Я][()!@#$%^&_=|\\a-zA-Zа-яА-Я+\-/*]', formula):
            raise SyntaxError(f"ERROR! Невірно введена формула, ви ввели {formula}")
        else:
            result = eval(formula)
        print(f"Результат обчислення {formula} = {result}")
        return result
    except SyntaxError as error:
        print(error)
