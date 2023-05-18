from Lesson_11.class_house import House


class SmallHouse(House):
    def __init__(self, price: int = 30000):
        super().__init__(area=40, price=price)
