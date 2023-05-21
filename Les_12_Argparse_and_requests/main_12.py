from Les_12_Argparse_and_requests.argparse_quadratic_equation import args
from quadratic_equation import calculate_quadratic_equation
from requests_pilots import get_millennium_falcon, millennium_falcon_json

if __name__ == "__main__":

    print("---------------------------------------------Завдання 1---------------------------------------------")
    try:

        results = calculate_quadratic_equation(args.a, args.b, args.c)

    except Exception as error:
        print(error)

    print("---------------------------------------------Завдання 2---------------------------------------------")
    try:

        result = get_millennium_falcon()
        millennium_falcon_json(result)

    except Exception as error:
        print(error)
