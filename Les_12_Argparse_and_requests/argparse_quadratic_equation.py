"""

Використовуючи модуль argparse створити програму розрахунку квадратного рівняння.
(Реалізацію самого рівняння можете взяти з минулих ДЗ)
Запуск програми python main.py -a={} -b={} c={} де параметри (a, b, c - параметри квадратного рівняння),
за замовчуванням параметр а = 0
При виклику програми з прапорцем --help вивести інформацію про програму та про параметри

cd Les_12_Argparse_and_requests/
python -i argparse_quadratic_equation.py --a 3 --b 4 --c 5
python argparse_quadratic_equation.py --a 1 --b 4 --c 8
python argparse_quadratic_equation.py --a 1 --b 14 --c 8
python argparse_quadratic_equation.py  --help

"""
import argparse

parser = argparse.ArgumentParser(description="Квадратне рівняння")

parser.add_argument("--a", type=float, default=0, help="Аргумент а (за замовчуванням = 0)")
parser.add_argument("--b", type=float, required=True, help="Аргумент b - обовʼязковий")
parser.add_argument("--c", type=float, required=True, help="Аргумент c - обовʼязковий")

args = parser.parse_args()
