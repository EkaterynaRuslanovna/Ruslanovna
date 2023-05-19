"""

Знайти найуспішнішого менеджера за підсумковою сумою продажів.
Як відповідь потрібно через пробіл вказати спершу його ім'я,
потім прізвище і після загальну суму його продажів.Файл manager_sales.json

"""
import json


def find_manager(name_of_file):
    with open(name_of_file, "r") as file:
        data = json.load(file)

    top_manager_name = ""
    top_manager_surname = ""
    total = 0

    for manager_object in data:
        calc_sum = sum([car["price"] for car in manager_object["cars"]])
        if calc_sum > total:
            total = calc_sum
            top_manager_name = manager_object["manager"]["first_name"]
            top_manager_surname = manager_object["manager"]["last_name"]

    print(f"Імʼя: {top_manager_name}, Прізвище: {top_manager_surname}, Загальна сума продажів: {total}")
