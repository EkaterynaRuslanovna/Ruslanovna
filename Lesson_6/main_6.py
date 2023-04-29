from random import randint
import Task_1
import Task_2
import Task_3
from Generate_random_list_with_different_types import generate_random_list_with_different_types
import Task_4
import Task_5
import json
import Task_6
from Additional_task_with_operands import calculate


if __name__ == '__main__':
    try:
        print("---------------------------------------------Завдання 1---------------------------------------------")
        number = randint(0, 1000)
        Task_1.is_the_number_an_exact_power_of_2(number)

        print("---------------------------------------------Завдання 2---------------------------------------------")
        number = randint(0, 1000)
        Task_2.square(number)

        print("---------------------------------------------Завдання 3---------------------------------------------")
        number = randint(2, 1000)
        if Task_3.is_prime(number):
            print(f"Число {number} є просте")
        else:
            print(f"Число {number} не є простим")

        print("---------------------------------------------Завдання 4---------------------------------------------")
        len_list = randint(2, 50)
        lst = generate_random_list_with_different_types(len_list)

        print(f"Початковий список: \n{lst}")
        print(f"\nЗмінений список: \n{Task_4.change_list(lst)}")

        print("---------------------------------------------Завдання 5---------------------------------------------")
        print(json.dumps(Task_5.to_dict(lst), indent=2))

        print("---------------------------------------------Завдання 6---------------------------------------------")
        start = randint(-100, 100)
        end = randint(-100, 100)
        print(f"Сума чисел від {start} до {end} = {Task_6.sum_range(start, end)}")

        print("---------------------------------------------Завдання 7---------------------------------------------")

        formula = input("Введіть математичний вираз: ")
        calculate(formula)

    except TypeError:
        print("ERROR: Функція повинна приймати необхідну кількість аргументів")

print("------------------------------------------------END-------------------------------------------------")