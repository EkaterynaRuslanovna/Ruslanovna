import datetime

# Створити декоратор який вимірює час виконання функції


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        end = datetime.datetime.now()
        delta = end - start
        print(f"Час Виконання функції {func.__name__} {delta} секунд")
    return wrapper


@measure_time
def for_test_func():
    result = any([True for i in range(100000000) if i // 3 == 0])
    return result

