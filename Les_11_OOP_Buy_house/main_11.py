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

3. В конструкції реалізувати:
    a. Викличте довідковий метод default_info() для класу Human()
    b. Створіть об'єкт класу Human
    c. Виведіть довідкову інформацію про створений об'єкт (викличте метод info()).
    d. Створіть об'єкт класу SmallHouse
    e. Спробуйте купити створений будинок, переконайтеся в отриманні попередження.
    f. Виправте фінансове становище об'єкта - викличте метод earn_money()
    g. Знову спробуйте купити будинок
    h. Подивіться, як змінилося стан об'єкта класу Human

"""
from Les_11_OOP_Buy_house.class_house import House
from Les_11_OOP_Buy_house.class_human import Human
from Les_11_OOP_Buy_house.class_smallHouse import SmallHouse


if __name__ == '__main__':

    try:

        print(f"Викличте довідковий метод default_info() для класу Human():")
        Human.default_info()

        print(f"\nСтворіть об'єкт класу Human:")
        human = Human(name="Kate", age=28)

        print(f"{human}")

        print(f"\nВиведіть довідкову інформацію про створений об'єкт (викличте метод info()):")
        human.info()

        print(f"\nЗмінити дані покупця:")
        human.change_info(name="Kateryna")
        human.info()

        print(f"\nСтворіть об'єкт класу SmallHouse:")
        small_house = SmallHouse(price=30000)
        small_house.show_the_characteristics_of_the_house()

        print(f"\nСтворіть об'єкт класу House:")
        house = House(area=120, price=280000)
        house.show_the_characteristics_of_the_house()

        print(f"\nСпробуйте купити створений будинок, переконайтеся в отриманні попередження:")
        human.buy_house(small_house, 50)
        human.buy_house(house, 100)

        print(f"\nВиправте фінансове становище об'єкта - викличте метод earn_money():")
        human.earn_money(120000)

        print(f"\nЗнову спробуйте купити будинок:")
        human.buy_house(small_house, 50)

        print(f"\nПодивіться, як змінився стан об'єкта класу Human:")
        human.info()

    except Exception as error:
        print(error)
