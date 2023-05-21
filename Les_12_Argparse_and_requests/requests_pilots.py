"""

https://swapi.dev/

Уважно вивчіть документацію цього API (https://swapi.dev/documentation) і напишіть програму,
яка виводить на екран (і JSON-файл) інформацію про пілотів легендарного корабля Millennium Falcon.

Інформація про корабель має містити такі пункти:
    назва,
    максимальна швидкість,
    клас,
    список пілотів.

Усередині списку про кожен пілот має бути така інформація:
    ім'я,
    зріст,
    вага,
    рідна планета,
    посилання на інформацію про рідну планету.

"""
import requests
import json

url = "https://swapi.dev/api/"
endpoint = "starships/"
params = {"search": "Millennium"}


def get_millennium_falcon():
    response = requests.get(url + endpoint, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['count'] == 1:
            millennium_falcon_info = {
                "Назва": data["results"][0]["name"],
                "Максимальна швидкість":  data["results"][0]["max_atmosphering_speed"],
                "Клас": data["results"][0]["starship_class"],
                "Список пілотів": get_pilots(data["results"][0]["pilots"])
            }
            return millennium_falcon_info


def get_pilots(pilots_urls: list):
    pilots_info = []
    for pilot_url in pilots_urls:
        response = requests.get(pilot_url)
        if response.status_code == 200:
            data = response.json()
            pilot_info = {
                "Імʼя": data["name"],
                "Зріст": data["height"],
                "Вага": data["mass"],
                "Рідна планета": get_homeworld(data["homeworld"]),
                "Посилання на інформацію про рідну планету": data["homeworld"]
            }
            pilots_info.append(pilot_info)
    return pilots_info


def get_homeworld(homeworld_url: str):
    response = requests.get(homeworld_url)
    if response.status_code == 200:
        data = response.json()
        homeworld_info = {
            "Назва": data['name']
        }
        return homeworld_info


def millennium_falcon_json(ship_info: dict):
    if ship_info:
        print("Millennium Falcon:")
        print("Назва:", ship_info['Назва'])
        print("Максимальна швидкість:", ship_info['Максимальна швидкість'])
        print("Клас:", ship_info['Клас'])
        print("Пілоти:")
        for pilot in ship_info['Список пілотів']:
            print("\tІмʼя:", pilot['Імʼя'])
            print("\tЗріст:", pilot['Зріст'])
            print("\tВага:", pilot['Вага'])
            print("\tРідна планета:", pilot['Рідна планета']['Назва'])
            print("\tПосилання на інформацію про рідну планету:", pilot['Посилання на інформацію про рідну планету'],"\n")

        with open('../Les_12_Argparse_and_requests/millennium_falcon.json', 'w', encoding="utf-8") as json_file:
            json.dump(ship_info, json_file, indent=4, ensure_ascii=False)
        print("Інформація успішно записала у файл 'millennium_falcon.json'.")
    else:
        print("Неочікувана помилка. Перевірте, можливо відсутні дані про starships")
