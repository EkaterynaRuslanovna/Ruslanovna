"""

4.Написать калькулятор с основными операциями(+, -, *, /)
Користувач вводить два числа та арифметичну операцію

"""

x = float(input("Введіть перше число:"))
y = float(input("Введіть друге число:"))

operand = input("Введіть операцію, яку треба виконати: (+, -, *, /)")


def calc(x, y, operation):
    try:
        if operation == "+":
            return x + y
        elif operation == "-":
            return x - y
        elif operation == "*":
            return x * y
        elif operation == "/":
            if y == 0:
                return print("Ділення на 0 неможливе")
            else:
                return x / y
        else:
            return print("Введено невірний знак арифметичної операції.")
    except ValueError:
        print("Введено невірне значення числа.")


result = calc(x, y, operand)
if result is not None:
    print(f"Результат: {result}")
