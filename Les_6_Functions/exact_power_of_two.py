"""

1. Дано натуральне число N.
Виведіть слово YES, якщо число N є точним ступенем двійки, або слово NO інакше.
8 - YES, 3 - NO

"""
from math import log2


def is_the_number_an_exact_power_of_2(number: int):
    try:
        power = log2(number)
        if power.is_integer():
            print("YES")
        else:
            print("NO")
    except TypeError:
        print(f"ERROR! Функція is_the_number_an_exact_power_of_2 приймає лише значення типу int, ви ввели {type(number)}")
    except ValueError:
        print(f"ERROR! Аргументом не може бути значення менше 1, ви ввели {number}")
