"""

5. Створіть англо-німецький словник, який називається e2g, і виведіть його на екран.
Слова для словника: stork / storch, hawk / falke, woodpecker / specht і owl / eule.
Виведіть німецький варіант слова owl. Додайте у словник, на ваш вибір, ще два слова та їхній переклад.
Виведіть окремо: словник; ключі і значення словника у вигляді списків.

"""
import json


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
