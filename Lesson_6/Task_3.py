# 3. Напишіть функцію is_prime, яка приймає 1 аргумент - число від 2 до 1000,
# і повертає True, якщо це просте число, і False в іншому випадку.

def is_prime(number: int):
    try:
        if 2 <= number <= 1000:
            if number == 2:
                return True
            if number % 2 == 0 or number == 1:
                return False
            for i in range(2, number):
                if number % i == 0:
                    return False
        else:
            raise ValueError(f"ERROR! Число повинно бути в діапазоні від 2 до 1000 включно, ви ввели {number}")
    except TypeError:
        print(f"ERROR! Функція is_prime приймає лише значення типу int, ви ввели {type(number)}")
    except ValueError as error:
        print(error)

