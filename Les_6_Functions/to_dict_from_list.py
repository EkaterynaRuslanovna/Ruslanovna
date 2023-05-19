"""

5. Напишіть функцію to_dict(lst),
яка приймає аргумент у вигляді списку і повертає словник, в якому кожен елемент списку є ключем і значенням.
Передбачається, що елементи списку відповідатимуть правилам завдання ключів у словниках.

"""


def to_dict(lst: list):
    try:
        if isinstance(lst, list):
            dictionary = {}
            for element in lst:
                dictionary[element] = element
            return dictionary
        else:
            raise TypeError(f"ERROR! Функція to_dict приймає лише значення типу list, ви ввели {type(lst)}")
    except TypeError as error:
        print(error)
