from random import choice
from random import randint


def generate_random_list_with_different_types(len_list):
    types = [int, str, bool]
    lst = []
    for current_type in range(len_list):
        element_type = choice(types)
        if element_type == int:
            element = randint(-100, 100)
        elif element_type == str:
            element = ''.join(choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
        else:
            element = choice([True, False])
        lst.append(element)
    return lst

