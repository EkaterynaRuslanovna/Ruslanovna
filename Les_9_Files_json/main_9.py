from group_people_json import find_droup
from manager_sales_json import find_manager


if __name__ == '__main__':
    print("---------------------------------------------Завдання 1---------------------------------------------")

    name_of_file = "group_people.json"

    try:
        find_droup(name_of_file)
    except FileNotFoundError:
        print(f'Файл з іменем {name_of_file} відсутній')
    except UnicodeDecodeError:
        print(f'Неможливо прочитати файл {name_of_file}')
    except (OSError, IOError) as error:
        print(f'Неочікувана помилка під час виконання {name_of_file}\nError: {error}')
    except Exception as error:
        print(error)

    print("---------------------------------------------Завдання 2---------------------------------------------")

    name_of_file = "manager_sales.json"

    try:
        find_manager(name_of_file)
    except FileNotFoundError:
        print(f'Файл з іменем {name_of_file} відсутній')
    except UnicodeDecodeError:
        print(f'Неможливо прочитати файл {name_of_file}')
    except (OSError, IOError) as error:
        print(f'Неочікувана помилка під час виконання {name_of_file}\nError: {error}')
    except Exception as error:
        print(error)
