# 1. Написать свой тип данных для сложения и вычитания, сравнение комплексных чисел.
# А так же правильного отображение их в консоли(magic method __str__)

"""
Комплексные числа - это числа, которые содержат две части: вещественную и мнимую.
Вещественная часть - это обычное действительное число, которое мы обычно используем в математике.
Мнимая часть - это число, которое умножается на "i", где "i" - это мнимая единица, которая определяется как корень из -1.
Комплексное число записывается в виде "a + bi", где "a" и "b" - это вещественные числа.
Например, комплексное число 3 + 2i имеет вещественную часть 3 и мнимую часть 2i.
Операции с комплексными числами включают сложение, вычитание, умножение и деление.
Эти операции выполняются с помощью правил алгебры и мнимой единицы "i".
Сложение: (a + bi) + (c + di) = (a + c) + (b + d)i
Вычитание: (a + bi) - (c + di) = (a - c) + (b - d)i
Сравнение: (a + bi) = (c + di) если и только если a = c и b = d
"""


class ComplexNumber:
    def __init__(self, real_number: int, number_that_is_multiplied_by_i: int):
        self.real_number = real_number
        self.number_that_is_multiplied_by_i = number_that_is_multiplied_by_i

    def __add__(self, other):
        first_part = self.real_number + other.real_number
        second_part = self.number_that_is_multiplied_by_i + other.number_that_is_multiplied_by_i
        return ComplexNumber(first_part, second_part)

    def __sub__(self, other):
        first_part = self.real_number - other.real_number
        second_part = self.number_that_is_multiplied_by_i - other.number_that_is_multiplied_by_i
        return ComplexNumber(first_part, second_part)

    def __eq__(self, other):
        return self.real_number == other.real_number and self.number_that_is_multiplied_by_i == other.number_that_is_multiplied_by_i

    def __str__(self):
        sign = "+" if self.number_that_is_multiplied_by_i >= 0 else "-"
        return f"{self.real_number} {sign} {abs(self.number_that_is_multiplied_by_i)}i"
