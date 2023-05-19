"""

Знайти ідентифікатор групи, де знаходиться найбільша кількість жінок, народжених після 1977 року.
Як відповідь необхідно вказати через пробіл ідентифікатор знайденої групи і скільки в ній було жінок,
народжених після 1977 року. Файл group_people.json

"""
import json


def find_droup(name_of_file):
    with open(name_of_file, "r") as file:
        data = json.load(file)

    group_id = 0
    counter = 0

    for group in data:
        count = 0
        for person in group["people"]:
            if person["gender"] == "Female" and person["year"] > 1977:
                count += 1
        if count > counter:
            counter = count
            group_id = group['id_group']

    print(f"Ідентифікатор групи: {group_id}, Кількість жінок, народжених після 1977 року: {counter}")
