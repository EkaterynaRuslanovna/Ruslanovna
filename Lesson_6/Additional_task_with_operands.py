# Реализовать так, чтоб если пользователь из клавиатуры вводит математический знак, то он не превращался в string


def calculate(formula):
    try:
        for item in formula:
            if item in "+-*/":
                operator = item
                num1, num2 = formula.split(operator)
                break
        else:
            raise ValueError("Оператор не знайдений")
        try:
            num1 = float(num1)
            num2 = float(num2)
            result = eval(formula)
            return result
        except ValueError:
            print(f"Невірно введені аргументи, ви ввели {num1} та {num2}")

    except ZeroDivisionError:
        print("Ділення на ноль неможливе")
    except ValueError as error:
        print(error)
    except TypeError as error:
        print(error)
