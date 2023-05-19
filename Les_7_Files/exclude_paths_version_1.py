"""

Написать скрипт, который подсчитает количество папок и файлов по заданному пути.
Если такого нет, то по всей системе(/ - для линукс/мак. Диск С - для виндоус).
Для удобства можно установить граничное значение числа папок(и/или файлов),
после которого скрипт не будет продолжать работу.
Среди найденных файлов показать самый большой и самый маленький по размеру, а так же с самым длинным и коротким именем.
Если во время работы скрипт был прерван(KeyboardInterrupt), то промежуточные результаты сериализуются в файл
и при повторном запуске эти пути исключаются из проверки.

"""
import os
import json


def read_exclude_paths():
    exclude_paths = set()
    if os.path.exists("exclude_paths.json"):
        with open("exclude_paths.json", "r") as file:
            exclude_paths = set(json.load(file))
    return exclude_paths


def write_exclude_paths(exclude_paths):
    with open("exclude_paths.json", "w") as file:
        json.dump(list(exclude_paths), file)


def count_folders_and_files(path, exclude_paths, MAX_COUNT):
    results = {"folders_count": 0, "files_count": 0, "max_size": 0, "min_size": 0, "max_name_len": 0, "min_name_len": 0}
    try:
        for root, dirs, files in os.walk(path):
            if root in exclude_paths:
                continue
            if results["files_count"] + len(files) > MAX_COUNT:
                break
            results["folders_count"] += len(dirs)
            for file in files:
                file_path = os.path.join(root, file)
                if file_path in exclude_paths:
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

                exclude_paths.update(set(os.path.join(root, dirs) for dirs in dirs))
            exclude_paths.update(set(os.path.join(root, files) for files in files))

    except KeyboardInterrupt:
        write_exclude_paths(exclude_paths)
        return None

    write_exclude_paths(exclude_paths)
    return {
        "folders_count": results['folders_count'],
        "files_count": results['files_count'],
        "max_size": results['max_size'],
        "min_size": results['min_size'],
        "max_name_len": results['max_name_len'],
        "min_name_len": results['min_name_len']
    }
