from task_1 import for_test_func
from task_2 import args_kwargs, concatinate_args_kwargs

if __name__ == '__main__':
    print("---------------------------------------------Завдання 1---------------------------------------------")

    try:
        for_test_func()
    except Exception as error:
        print(error)

    print("---------------------------------------------Завдання 2---------------------------------------------")

    try:
        args_kwargs(1, 2, 3, 4, c=5, d=6)
        concatinate_args_kwargs("Vadym,", "phone - ", 380939157605, "@mastaforka", day=16, month="July")
    except Exception as error:
        print(error)