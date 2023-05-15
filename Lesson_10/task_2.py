# Створити декоратор який кожен раз буде записувати у файл результат роботи якоїсь функції після її виклику
# (наприклад функція яка прораховує суму всіх переданих аргументів *args).
# Запис в файл формату ""Function launched at {час запуску} with result {результат роботи функції}

def result_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        total = sum(args) + sum(kwargs.values())
        with open("func_results.txt", "a") as file:
            file.write(f"Сума всіх аргументів функції: {str(total)}\n")
        return result
    return wrapper


def write_results_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("write_results.txt", "a") as file:
            file.write(f"Результат виконання функції {func.__name__}: {result} \n")
        return result
    return wrapper


@result_decorator
def args_kwargs(*args, **kwargs):
    return args, kwargs


@write_results_decorator
def concatinate_args_kwargs(*args, **kwargs):
    args_list = [str(arg) for arg in args]
    kwargs_list = [f"{key}={value}" for key, value in kwargs.items()]
    all_args = args_list + kwargs_list
    return " ".join(all_args)
