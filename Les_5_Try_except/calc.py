"""

3. Напишіть інтерактивний калькулятор.
Передбачається, що користувач вводить формулу, що складається з числа, оператора (як мінімум + і -) та іншого числа,
розділених пробілом (наприклад, 1 + 1). Використовуйте str.split()

a. Якщо вхідні дані не складаються з трьох елементів, генеруйте ексепшн FormulaError.
b. Спробуйте перетворити перший і третій елемент на float (float_value = float(str_value)).
Спіймайте будь-яку ValueError і згенеруйте замість нього FormulaError
c. Якщо другий елемент не є «+» або «-», киньте ексепшн FormulaError

"""


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



