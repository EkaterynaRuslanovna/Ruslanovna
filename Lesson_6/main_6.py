from random import randint
import task_1
import task_2
import task_3
from generate_random_list_with_different_types import generate_random_list_with_different_types
import task_4
import task_5
import json
import task_6
from additional_task_with_operands import calculate


if __name__ == '__main__':
    print("---------------------------------------------Завдання 1---------------------------------------------")

    try:
        number = randint(0, 1000)
        Task_1.is_the_number_an_exact_power_of_2(number)
    except TypeError:
        print(f"ERROR! Функція is_the_number_an_exact_power_of_2 повинна приймати 1 аргумент 'number'")

    print("---------------------------------------------Завдання 2---------------------------------------------")

    try:
        side_of_the_square = randint(0, 1000)
        print(Task_2.square(side_of_the_square))
    except TypeError:
        print(f"ERROR! Функція square повинна приймати 1 аргумент 'number'")

    print("---------------------------------------------Завдання 3---------------------------------------------")

    try:
        number = randint(2, 1000)
        print(Task_3.is_prime(number))
    except TypeError:
        print(f"ERROR! Функція is_prime повинна приймати 1 аргумент 'number'")

    print("---------------------------------------------Завдання 4---------------------------------------------")

    try:
        len_list = randint(2, 50)
        lst = generate_random_list_with_different_types(len_list)

        print(Task_4.change_list(lst))
    except TypeError:
        print(f"ERROR! Функція change_list повинна приймати 1 аргумент 'lst'")

    print("---------------------------------------------Завдання 5---------------------------------------------")

    try:
        print(json.dumps(Task_5.to_dict(lst), indent=2))
    except TypeError:
        print(f"ERROR! Функція to_dict повинна приймати 1 аргумент 'lst'")

    print("---------------------------------------------Завдання 6---------------------------------------------")

    try:
        start = randint(-100, 100)
        end = randint(-100, 100)

        print(Task_6.sum_range(start, end))
    except TypeError:
        print(f"ERROR! Функція sum_range повинна приймати 2 аргументи 'int'")

    print("---------------------------------------------Завдання 7---------------------------------------------")

    formula = input("Введіть математичний вираз: ")
    calculate(formula)

print("------------------------------------------------END-------------------------------------------------")