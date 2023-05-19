"""

2. Створити реалізацію квадратного рівняння a•x²+b•x+c=0(користувач вводить a, b, c),
якщо дискримінант від'ємний викликати виняток DiscriminantError і вивести відповідне повідомлення.

"""


class DiscriminantError(Exception):
    pass


try:
    a, b, c = float(input("Введіть значення a: ")), float(input("Введіть значення b: ")), float(input("Введіть значення c: "))
    D = b ** 2 - 4 * a * c

    if D < 0:
        raise DiscriminantError(f"Дискримінант = {D}; Дане рівняння немає коренів.")
    elif D == 0:
        x = (- b) / 2 * a
        print(f"Корінь рівняння х = {x}")
    else:
        x1 = ((- b) + D ** 0.5) / 2 * a
        x2 = ((- b) - D ** 0.5) / 2 * a
        print(f"Корінь рівняння х1 = {x1}, корінь рівняння х2 = {x2}")

except ValueError as error:
    print("Введіть числове значення!")
except DiscriminantError as error:
    print(error)
