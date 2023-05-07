import os
import csv

# Открыть файл test_file.csv, прочитать,
# распарсить зп сотрудников в долларах и перевести в гривны на текущую дату(курс задается отдельной переменной).
# Результат сохранить в новый файл salaries_uah.csv


USD = 36.57


def searching_file(file_name: str, current_dir=None):
    if current_dir is None:
        current_dir = os.getcwd()
    content = os.scandir(current_dir)
    for item in content:
        if item.name == file_name:
            return item.path
        elif item.is_dir():
            file = searching_file(file_name, item.path)
            if file:
                return file
    return None


def create_file_with_converting_salaries(file_name):
    with open(file_name, 'r') as file:
        with open('salaries_uah.csv', 'w', newline='') as new_file:
            reader = csv.reader(file)
            writer = csv.writer(new_file)
            headers = next(reader)
            writer.writerow(headers)
            for row in reader:
                new_row = []
                for box in row:
                    if box.isdigit():
                        salary_usd = int(box)
                        salary_uah = salary_usd * USD
                        new_row.append(int(salary_uah))
                    else:
                        new_row.append(box)
                writer.writerow(new_row)


def convert_to_true_path(path_of_file):
    index_of_last_slash = path_of_file.rfind("/")
    if index_of_last_slash != -1:
        path_of_file = path_of_file[:index_of_last_slash]
    return path_of_file


# os.chdir("/Users/macbookpro/downloaded")
# name_of_file = "test_file.csv"
# current_directory = os.getcwd()
# print(current_directory)


# try:
#     file_path = searching_file(name_of_file)
#     file_path = convert_to_true_path(file_path)
#
#     os.chdir(file_path)
#
#     create_file_with_converting_salaries(name_of_file)
#
# except FileNotFoundError:
#     print(f'Файл з іменем {name_of_file} відсутній')
# except UnicodeDecodeError:
#     print(f'Неможливо прочитати файл {name_of_file}')
# except (OSError, IOError) as error:
#     print(f'Неочікувана помилка під час виконання {name_of_file}\nError: {error}')
