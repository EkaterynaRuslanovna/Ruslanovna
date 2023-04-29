# Реализовать так, чтоб если пользователь из клавиатуры вводит математический знак, то он не превращался в strin


def calculate(formula):
    try:
        result = eval(formula)
        print(f"Результат обчислення {formula} = {result}")
        return result
    except Exception as error:
        print(error)