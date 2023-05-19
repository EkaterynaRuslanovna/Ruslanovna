"""

4. Створіть словник з чотирма назвами мов програмування (ключі) та іменами розробників цих мов (значення).
Виведіть по черзі для усіх елементів словника повідомлення типу My favorite programming language is Python.
It was created by Guido van Rossum.. Видаліть, на ваш вибір, одну пару «мова: розробник» із словника.
Виведіть словник на екран.

"""
import json

languages = {"Python": "Guido van Rossum", "JavaScript": "Brendan Eich", "C++": "Bjarne Stroustrup", "C#": "Anders Hejlsberg"}
print(json.dumps(languages, indent=2), "\n")

for key, value in languages.items():
    print(f"My favorite programming language is {key}. It was created by {value}.")

languages.pop("C++", None)
print("\n", json.dumps(languages, indent=2))
