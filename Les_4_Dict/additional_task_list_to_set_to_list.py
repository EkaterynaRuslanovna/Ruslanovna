"""

8. Есть лист например: 33, 2, 44, 2, 15, 34, 33. Нужно превратить его в сет, чтоб избавиться от дубликатов.
Вернуть список в том же порядке, как и был, но без дубликатов уже, то бишь: 33, 2, 44, 15, 34

"""

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
