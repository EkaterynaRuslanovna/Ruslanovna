print("--------------------------------------------------Завдання 1--------------------------------------------------")

# 1. Створити проект на github, "залити" на віддалений репозиторій всі свої ДЗ до 5-ї лекції

print("DONE")


print("--------------------------------------------------Завдання 2--------------------------------------------------")

# 2. Створити реалізацію квадратного рівняння a•x²+b•x+c=0(користувач вводить a, b, c),
# якщо дискримінант від'ємний викликати виняток DiscriminantError і вивести відповідне повідомлення.


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


print("--------------------------------------------------Завдання 3--------------------------------------------------")


# 3. Напишіть інтерактивний калькулятор.
# Передбачається, що користувач вводить формулу, що складається з числа, оператора (як мінімум + і -) та іншого числа,
# розділених пробілом (наприклад, 1 + 1). Використовуйте str.split()

# a. Якщо вхідні дані не складаються з трьох елементів, генеруйте ексепшн FormulaError.
# b. Спробуйте перетворити перший і третій елемент на float ( float_value = float(str_value)).
# Спіймайте будь-яку ValueError і згенеруйте замість нього FormulaError
# c. Якщо другий елемент не є «+» або «-», киньте ексепшн FormulaError

class FormulaError(Exception):
    pass


def calc(x, operator, y):
    result = None
    match operator:
        case "+":
            result = x + y
        case "-":
            result = x - y
        case "*":
            result = x * y
        case "/":
            result = x / y
        case "**":
            result = x ** y
    if not result:
        raise FormulaError(f"FormulaError: Неможливо виконати операцію з даним оператором {operator}. Введіть існуючий оператор (+, -, *, /, **)")
    print(f"Результат обчислення {x} {operator} {y} = {result}")


try:
    formula = (input("Введіть формулу для розрахунку: ")).split()
    if len(formula) != 3:
        raise FormulaError(f"FormulaError: Невірна кількість елементів. Ви ввели {len(formula)} елементи. Введіть 3 елементи.")

    try:
        x, operator, y = formula
        x = float(x)
        y = float(y)
        calc(x, operator, y)
    except ValueError:
        raise FormulaError("FormulaError: Некоректні вхідні дані!")
except FormulaError as error:
    print(error)


print("--------------------------------------------------Завдання 4--------------------------------------------------")

# 4. Задачі на github відправити окремими коммітами.

print("DONE")



