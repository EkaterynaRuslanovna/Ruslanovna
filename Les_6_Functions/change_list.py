"""

4.Напишіть функцію change_list, яка приймає список і змінює місця його перший і останній елемент.
У вихідному списку щонайменше 2 елементи.

"""


def change_list(lst: list):
    try:
        if not isinstance(lst, list):
            raise TypeError(f"ERROR! Функція change_list приймає лише значення типу list, ви ввели {type(lst)}")
        if len(lst) < 2:
            raise ValueError(f"ERROR! Функція change_list приймає у вихідному списку мінімум 2 елементи, у вашому списку {len(lst)}")
        else:
            lst[0], lst[-1] = lst[-1], lst[0]
            return lst
    except ValueError as error:
        print(error)
    except TypeError as error:
        print(error)
