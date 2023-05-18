from Lesson_11.class_house import House


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
        print(f"Ви отримали зарплату у розмірі {salary}$.")

    def buy_house(self, house: House, discount: int = 0):
        final_price = house.final_price(discount)
        if self._money >= final_price:
            self._make_deal(house, final_price)
            print(f"Вітаємо, ви успішно придбали будинок! На вашому рахунку залишилось {self._money}$")
        else:
            print(f"Недостатньо грошей! На вашому рахунку {self._money}$")