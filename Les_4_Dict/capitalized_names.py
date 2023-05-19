"""
1. Існує список з іменами ["john", "marta", "james", "amanda", "marianna"],
перетворити рядок, щоб кожне ім'я явно починалися з великої літери.

"""

names = ["john", "marta", "james", "amanda", "marianna"]
print("Було: ", names)
names = [name.title() for name in names]
print("Стало: ", names)
