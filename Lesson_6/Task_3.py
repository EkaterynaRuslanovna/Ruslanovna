# 3. Напишіть функцію is_prime, яка приймає 1 аргумент - число від 2 до 1000,
# і повертає True, якщо це просте число, і False в іншому випадку.

def is_prime(number):
    if number == 2:
        return True
    if number % 2 == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
