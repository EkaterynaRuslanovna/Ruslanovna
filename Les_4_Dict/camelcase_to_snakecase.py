"""

3. У вас є список змінних у форматі CamelCase ["FirstItem", "FriendsList", "MyTuple"],
перетворити його у список змінних для Пайтона snake_case, "friends_list", "my_tuple"]

"""

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
