import os
from task_1 import searching_file
from task_1 import create_file_with_converting_salaries
from task_1 import convert_to_true_path
from task_2_Version_1_ import read_exclude_paths
from task_2_Version_1_ import count_folders_and_files

if __name__ == '__main__':
    print("---------------------------------------------Завдання 1---------------------------------------------")

    USD = 36.57

    os.chdir("/Users/macbookpro/downloaded")
    name_of_file = "test_file.csv"
    current_directory = os.getcwd()

    try:
        file_path = searching_file(name_of_file)
        file_path = convert_to_true_path(file_path)

        os.chdir(file_path)

        create_file_with_converting_salaries(name_of_file)

    except FileNotFoundError:
        print(f'Файл з іменем {name_of_file} відсутній')
    except UnicodeDecodeError:
        print(f'Неможливо прочитати файл {name_of_file}')
    except (OSError, IOError) as error:
        print(f'Неочікувана помилка під час виконання {name_of_file}\nError: {error}')

    print("---------------------------------------------Завдання 2---------------------------------------------")

    os.chdir("/Users/macbookpro/Kate/Lesson_7")

    path = "/Users/macbookpro/PROJECTS/pythonProject"
    if not os.path.exists(path):
        path = "/Users/macbookpro"

    MAX_COUNT = 100

    exclude_paths = read_exclude_paths()
    print(count_folders_and_files(path, read_exclude_paths(), MAX_COUNT))