import argparse
from ..Les_5_Try_except.quadratic_equation import calculate_quadratic_equation


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Квадратне рівняння")

    parser.add_argument("-a", type=float, default=0, help="Аргумент а (за замовчуванням = 0)")
    parser.add_argument("-b", type=float, required=True, help="Аргумент b - обовʼязковий")
    parser.add_argument("-c", type=float, required=True, help="Аргумент c - обовʼязковий")

    args = parser.parse_args()

    results = calculate_quadratic_equation(args.a, args.b, args.c)
