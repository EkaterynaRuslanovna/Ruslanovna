"""    Купівля будинку

Опис класової структури

Є Людина, характеристиками якої є:
    Ім'я
    Вік
    Наявність грошей
    Наявність власного житла

Людина може:
    Надати інформацію про себе
    Заробити гроші
    Купити будинок

Також є Дім, до властивостей якого відносяться:
    Площа
    Вартість

Для Будинку можна:
    Застосувати знижку на покупку
    Також є невеликий типовий будинок, обов'язковою площею 40м2.

Завдання:

Клас Human

1. Створіть клас Human.
2. Визначте для нього два статичні атрибути: default_name та default_age.
3. Створіть метод __init__(), який, крім self, приймає ще два параметри: name і age.
Для цих параметрів вкажіть значення за замовчанням, використовуючи атрибути default_name та default_age.
У методі __init__() визначте чотири атрибути: Публічні - name та age. Приватні - money та house.
4. Реалізуйте довідковий метод info(), який виводитиме поля name, age, house і money.
5. Реалізуйте довідковий статичний метод default_info(), який виводитиме статичні атрибути default_name та default_age.
6. Реалізуйте приватний метод make_deal(), який відповідатиме за технічну реалізацію купівлі будинку:
зменшувати кількість грошей на рахунку та привласнювати посилання на щойно куплений будинок.
Як аргументи даний метод приймає об'єкт будинку та його ціну.
7. Реалізуйте метод earn_money(), який збільшує значення якості money.
8. Реалізуйте метод buy_house(), який перевірятиме, що людина має достатньо грошей для покупки, і здійснювати угоду.
Якщо грошей надто мало – потрібно вивести попередження в консоль.
Параметри методу: посилання на будинок та розмір знижки

"""
from Les_11_OOP_Buy_house.class_house import House


class Human:

    default_name = "Покупець"
    default_age = 18

    def __init__(self, name: str = default_name, age: int = default_age):
        self.name = name
        self.age = age
        self._money = 0
        self._houses = []

    def info(self):
        print(f"Імʼя: {self.name}")
        print(f"Вік: {self.age}")
        print(f"Баланс: {self._money}")
        print(f"Будинки: {self._houses}")

    def change_info(self, name: str = None, age: int = None):
        if name:
            self.name = name
        if age:
            self.age = age

    @staticmethod
    def default_info():
        print(f"Імʼя по замовчуванню: {Human.default_name}")
        print(f"Вік по замовчуванню: {Human.default_age}")

    def _make_deal(self, house: House, price: float):
        self._money -= price
        self._houses.append(house)

    def earn_money(self, salary: int = 1000):
        self._money += salary
        print(f"Ви отримали зарплату у розмірі {salary}$. На вашому балансі {self._money}$")

    def buy_house(self, house: House, discount: int = 0):
        final_price = house.final_price(discount)
        if self._money >= final_price:
            self._make_deal(house, final_price)
            print(f"Вітаємо, ви успішно придбали будинок! На вашому рахунку залишилось {self._money}$")
        else:
            print(f"Недостатньо грошей! На вашому рахунку {self._money}$")
