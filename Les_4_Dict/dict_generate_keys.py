"""

7. Напишіть програму, яка виводить словник, в якому ключі є числами від 1 до 15 (обидва включені),
а значення є квадратами ключів. Генерація ключів та значень має бути виконана через цикл.

"""
import json


values_in_squares_of_keys = {}

for key in range(1, 16):
    values_in_squares_of_keys[key] = key ** 2

print("Cловник з квадратами ключів: \n", json.dumps(values_in_squares_of_keys, indent=5))
