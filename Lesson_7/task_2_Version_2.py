import os
import json

# Написать скрипт, который подсчитает количество папок и файлов по заданному пути.
# Если такого нет, то по всей системе(/ - для линукс/мак. Диск С - для виндоус).
# Для удобства можно установить граничное значение числа папок(и/или файлов),
# после которого скрипт не будет продолжать работу.
# Среди найденных файлов показать самый большой и самый маленький по размеру, а так же с самым длинным и коротким именем.
# Если во время работы скрипт был прерван(KeyboardInterrupt), то промежуточные результаты сериализуются в файл
# и при повторном запуске эти пути исключаются из проверки.

path = "/Users/macbookpro/PROJECTS/pythonProject"
if not os.path.exists(path):
    path = "/Users/macbookpro"

MAX_COUNT = 100
EXCLUDE_PATHS = set()
results = {"folders_count": 0, "files_count": 0, "max_size": 0, "min_size": 0, "max_name_len": 0, "min_name_len": 0}

if os.path.exists("exclude_paths.json"):
    with open("exclude_paths.json", "r") as file:
        EXCLUDE_PATHS = set(json.load(file))
try:
    for root, dirs, files in os.walk(path):
        if root in EXCLUDE_PATHS:
            continue
        if results["files_count"] + len(files) > MAX_COUNT:
            break
        results["folders_count"] += len(dirs)
        for file in files:
            file_path = os.path.join(root, file)
            if file_path in EXCLUDE_PATHS:
                continue
            results["files_count"] += 1
            file_size = os.path.getsize(file_path)
            if results["max_size"] == 0 or file_size > results["max_size"]:
                results["max_size"] = file_size
            if results["min_size"] == 0 or file_size < results["min_size"]:
                results["min_size"] = file_size
            name_len = len(file)
            if results["max_name_len"] == 0 or name_len > results["max_name_len"]:
                results["max_name_len"] = name_len
            if results["min_name_len"] == 0 or name_len < results["min_name_len"]:
                results["min_name_len"] = name_len

            EXCLUDE_PATHS.update(set(os.path.join(root, dirs) for dirs in dirs))
        EXCLUDE_PATHS.update(set(os.path.join(root, files) for files in files))

except KeyboardInterrupt:
    with open("exclude_paths.json", "w") as file:
        json.dump(list(EXCLUDE_PATHS), file)

print(f"Кількість папок: {results['folders_count']}")
print(f"Кількість файлів: {results['files_count']}")
print(f"Найбільший файл: {results['max_size']} bytes")
print(f"Найменший файл: {results['min_size']} bytes")
print(f"Найдовша назва файлу: {results['max_name_len']} символів")
print(f"Найменша назва файлу: {results['min_name_len']} символів")