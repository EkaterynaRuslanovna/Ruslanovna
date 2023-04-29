from math import log2
# 1. Дано натуральне число N.
# Виведіть слово YES, якщо число N є точним ступенем двійки, або слово NO інакше.
# 8 - YES, 3 - NO


def is_the_number_an_exact_power_of_2(number: int):
    try:
        power = log2(number)
        if power.is_integer():
            print(f"YES. Число {number} є точним ступенем двійки")
        else:
            print(f"NO. Число {number} не є точним ступенем двійки")
    except TypeError:
        print("ERROR: Функція приймає лише значення типу int, окрім 0")
    except ValueError:
        print("ERROR: Аргументом не може бути значення менше 1")

