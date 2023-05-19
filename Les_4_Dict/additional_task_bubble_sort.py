"""

Написати сортування бульбашками

"""
import random


def do_bubble_sort(nums_list):
    flag = True
    while flag:
        flag = False
        for i in range(len(nums_list) - 1):
            if nums_list[i] > nums_list[i + 1]:
                nums_list[i], nums_list[i + 1] = nums_list[i + 1], nums_list[i]
                flag = True
    return nums_list


get_len = random.randint(5, 30)

nums_list = [random.randint(1, 100) for j in range(get_len)]
print(f"Начальный список:\n{nums_list}\n")

bubble_list = do_bubble_sort(nums_list)
print(f"Пузырьковая сортировка: \n{bubble_list}\n")
