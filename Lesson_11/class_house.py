class House:

    def __init__(self, area: float = 40, price: int = 50000):
        self._area = area
        self._price = price

    def final_price(self, discount: int = 0):
        if discount > 100:
            raise ValueError("Знижка не може бути більша, ніж 100%")
        elif discount < 0:
            raise ValueError("Знижка не може бути менша, ніж 0%")
        else:
            return self._price * (1 - (discount/100))

    def show_the_characteristics_of_the_house(self):
        print(f"Площа: {self._area}")
        print(f"Ціна: {self._price}")