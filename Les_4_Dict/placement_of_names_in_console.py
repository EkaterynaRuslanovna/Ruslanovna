"""

2. Є список друзів ["John", "Marta", "James", "Amanda", "Marianna"].
Виведіть імена в консолі, кожен з нового рядка, вирівнюючи праву сторону,
використовуючи метод рядка та форматування через F String.
Також над іменами першим рядком виведіть NAME, де NAME має бути посередині(string.center()),
а решта простору заповнена символом "*"

"""

names = ["John", "Marta", "James", "Amanda", "Marianna"]
print("NAME".center(100, "*"))

for friend in names:
    print(f"{friend:>100}")
