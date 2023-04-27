import json

print("--------------------------------------------------Завдання 1--------------------------------------------------")

# 1. Існує список з іменами ["john", "marta", "james", "amanda", "marianna"],
# перетворити рядок, щоб кожне ім'я явно починалися з великої літери.

names = ["john", "marta", "james", "amanda", "marianna"]
print("Було: ", names)
names = [name.title() for name in names]
print("Стало: ", names)


print("--------------------------------------------------Завдання 2--------------------------------------------------")

# 2. Є список друзів ["John", "Marta", "James", "Amanda", "Marianna"].
# Виведіть імена в консолі, кожен з нового рядка, вирівнюючи праву сторону,
# використовуючи метод рядка та форматування через F String.
# Також над іменами першим рядком виведіть NAME, де NAME має бути посередині(string.center()),
# а решта простору заповнена символом "*"

names = ["John", "Marta", "James", "Amanda", "Marianna"]
print("NAME".center(100, "*"))

for friend in names:
    print(f"{friend:>100}")


print("--------------------------------------------------Завдання 3--------------------------------------------------")

# 3. У вас є список змінних у форматі CamelCase ["FirstItem", "FriendsList", "MyTuple"],
# перетворити його у список змінних для Пайтона snake_case, "friends_list", "my_tuple"]

CamelCase = ["FirstItem", "FriendsList", "MyTuple"]
print("Було: ", CamelCase)

snake_case = []

for item in CamelCase:
    snake_word = ""
    for index, letter in enumerate(item):
        if letter.isupper() and index != 0:
            snake_word += "_" + letter.lower()
        else:
            snake_word += letter.lower()
    snake_case.append(snake_word)
print("Стало: ", snake_case)

print("--------------------------------------------------Завдання 4--------------------------------------------------")

# 4. Створіть словник з чотирма назвами мов програмування (ключі) та іменами розробників цих мов (значення).
# Виведіть по черзі для усіх елементів словника повідомлення типу My favorite programming language is Python.
# It was created by Guido van Rossum.. Видаліть, на ваш вибір, одну пару «мова: розробник» із словника.
# Виведіть словник на екран.

languages = {"Python": "Guido van Rossum", "JavaScript": "Brendan Eich", "C++": "Bjarne Stroustrup", "C#": "Anders Hejlsberg"}
print(json.dumps(languages, indent=2), "\n")

for key, value in languages.items():
    print(f"My favorite programming language is {key}. It was created by {value}.")

languages.pop("C++", None)
print("\n", json.dumps(languages, indent=2))

print("--------------------------------------------------Завдання 5--------------------------------------------------")

# 5. Створіть англо-німецький словник, який називається e2g, і виведіть його на екран.
# Слова для словника: stork / storch, hawk / falke, woodpecker / specht і owl / eule.
# Виведіть німецький варіант слова owl. Додайте у словник, на ваш вибір, ще два слова та їхній переклад.
# Виведіть окремо: словник; ключі і значення словника у вигляді списків.

e2g = {"stork": "storch", "hawk": "falke", "woodpecker": "specht", "owl": "eule"}
print(json.dumps(e2g, indent=1))
print(f"\nСлово 'owl' перекладається на німецьку, як: {e2g['owl']}")

e2g.update({"bird": "vogel", "butterfly": "schmetterling"})
print("\nПовний словник: ", json.dumps(e2g, indent=1))
print("\nКлючі словника: ", list(e2g.keys()))
print("Значення словника: ", list(e2g.values()))

e2g_lst_version_2 = []
e2g_lst_version_3 = []

for key, value in e2g.items():
    e2g_lst_version_2.append([f"\"{key}\": \"{value}\""])
    e2g_lst_version_3.append([{key: value}])
print("\nВерсія друга: ", e2g_lst_version_2)
print("Версія третя: ", e2g_lst_version_3)

print("--------------------------------------------------Завдання 6--------------------------------------------------")

# 6. Створіть багаторівневий словник subjects навчальних предметів.
# Використайте наступні рядки для ключів верхнього рівня: 'science', 'humanities' і 'public'.
# Зробіть так, щоб ключ 'science' був ім’ям іншого словника, який має ключі 'physics', 'computer science' і 'biology'.
# Зробіть, щоб ключ 'physics' посилався на список рядків зі значеннями 'nuclear physics', 'optics' і 'thermodynamics'.
# Решта ключів повинні посилатися на порожні словники.
# Виведіть на екран ключі subjects['science'] і значення subjects['science']['physics'].

subjects = {
    'science': {
        'physics': ['nuclear physics', 'optics', 'thermodynamics'],
        'computer science': {},
        'biology': {}
    },
    'humanities': {},
    'public': {}
}
print("Словник: \n", json.dumps(subjects, indent=5))
print("Ключі subjects['science']:  ", subjects["science"].keys(), "\n")
print("Значення subjects['science']['physics']:  ", subjects["science"]["physics"])

print("--------------------------------------------------Завдання 7--------------------------------------------------")

# 7. Напишіть програму, яка виводить словник, в якому ключі є числами від 1 до 15 (обидва включені),
# а значення є квадратами ключів. Генерація ключів та значень має бути виконана через цикл.

values_in_squares_of_keys = {}

for key in range(1, 16):
    values_in_squares_of_keys[key] = key ** 2

print("Cловник з квадратами ключів: \n", json.dumps(values_in_squares_of_keys, indent=5))


print(
    "----------------------------------------------Завдання 8 ДОДАТКОВЕ----------------------------------------------")

# 8. Есть лист например: 33, 2, 44, 2, 15, 34, 33. Нужно превратить его в сет, чтоб избавиться от дубликатов.
# Вернуть список в том же порядке, как и был, но без дубликатов уже, то бишь: 33, 2, 44, 15, 34


# version 1
lst = [33, 2, 21, 33, 44, 2, 15, 77, 34, 33]
print(lst)

new_lst = list(set(lst))
print(new_lst)

new_lst.sort(key=lst.index)
print(new_lst)

print("--------------------------------------------------------------------------------------------------------------")

# version 2
lst = [33, 2, 21, 33, 44, 2, 15, 77, 34, 33]
print(lst)

set_lst = set(lst)
print(set_lst)

new_lst = []
for item in lst:
    if item in set_lst:
        new_lst.append(item)
        set_lst.remove(item)

print(new_lst)


