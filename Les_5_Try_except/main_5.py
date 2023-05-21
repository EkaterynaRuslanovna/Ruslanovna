from quadratic_equation import calculate_quadratic_equation, DiscriminantError
from calc import calc, FormulaError

if __name__ == '__main__':

    try:
        a, b, c = float(input("Введіть значення a: ")), float(input("Введіть значення b: ")), float(
            input("Введіть значення c: "))

        calculate_quadratic_equation(a, b, c)
    except ValueError as error:
        print("Введіть числове значення!")
    except DiscriminantError as error:
        print(error)

    try:
        formula = (input("Введіть формулу для розрахунку: ")).split()
        if len(formula) != 3:
            raise FormulaError(
                f"FormulaError: Невірна кількість елементів. Ви ввели {len(formula)} елементи. Введіть 3 елементи.")

        try:
            x, operator, y = formula
            x = float(x)
            y = float(y)
            calc(x, operator, y)
        except ValueError:
            raise FormulaError("FormulaError: Некоректні вхідні дані!")
    except FormulaError as error:
        print(error)