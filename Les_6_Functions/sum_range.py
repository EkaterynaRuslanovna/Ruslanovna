"""

6.Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа від значення start до величини end включно.
Якщо користувач задасть перше число більше, ніж друге, просто поміняйте їх місцями.

"""


def sum_range(start: int, end: int):
    try:
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError(f"ERROR! Функція sum_range повинна приймати 2 аргументи 'int', ви ввели {start} - {type(start)} та {end} - {type(end)}")
        if start > end:
            raise ValueError("ERROR! Значення start не може бути більше значення end")
        else:
            total = 0
            for number in range(start, end + 1):
                total += number
            return total
    except TypeError as error:
        print(error)
    except ValueError as error:
        print(error)
