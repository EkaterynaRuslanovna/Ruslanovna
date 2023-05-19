"""

3. Написати програму для підрахунку конвертації валюти:
UAH --> USD
USD --> UAH
UAH --> EUR
EUR --> UAH

"""

USD = 36.57
EUR = 40.42

try:
    amount = float(input("Введіть суму: "))
    currency_from = int(
        input("Оберіть цифру від 1 до 3 з якої валюти конвертувати: \n1 - UAH, \n2 - USD, \n3 - EUR: \n"))
    currency_to = int(input("Оберіть цифру від 1 до 3 в яку конвертувати: \n1 - UAH, \n2 - USD, \n3 - EUR: \n"))

    if currency_from == 1 and currency_to == 2:
        print(f"{amount} UAH = {amount / USD} USD за курсом НБУ")
    elif currency_from == 2 and currency_to == 1:
        print(f"{amount} USD = {amount * USD} UAH за курсом НБУ")
    elif currency_from == 1 and currency_to == 3:
        print(f"{amount} UAH = {amount / EUR} EUR за курсом НБУ")
    elif currency_from == 3 and currency_to == 1:
        print(f"{amount} EUR = {amount * USD} UAH за курсом НБУ")
    elif currency_from == 2 and currency_to == 3:
        print(f"{amount} USD = {amount / 1.11} EUR за курсом НБУ")
    elif currency_from == 3 and currency_to == 2:
        print(f"{amount} EUR = {amount * 1.11} USD за курсом НБУ")
    else:
        print(f"Неможливо конвертувати обрані варіанти.")

except ValueError:
    print("Введено невірне значення суми або номеру валюти.")
