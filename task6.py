"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random

SIZE = 5
MAX_LIMIT = 50
MIN_LIMIT = -50
arr = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
# arr = [38, -2, 0, 42]

min_idx = None
max_idx = None
min_item = None
max_item = None
items_sum = None

print(f"Исходный массив: {arr}")

if len(arr) > 1:
    # обходим массив, находим min и max элементы и их индексы
    for idx, item in enumerate(arr):
        if min_item is None or min_item > item:
            min_item = item
            min_idx = idx
        elif max_item is None or max_item < item:
            max_item = item
            max_idx = idx

    print(f"Минимальный элемент: '{min_item}', на позиции {min_idx}")
    print(f"Максимальный элемент: '{max_item}', на позиции {max_idx}")

    # если начальный индекс больше конечного, то меняем местами
    if min_idx > max_idx:
        min_idx, max_idx = max_idx, min_idx

    # суммируем элементы между min и max лементами исключительно
    for idx in range(min_idx+1, max_idx):
        if items_sum is None:
            items_sum = arr[idx]
        else:
            items_sum += arr[idx]

    if items_sum is not None:
        print(f"Сумма элементов между min и max = {items_sum}")
    else:
        print(f"min и max элементы находятся рядом")
else:
    print(f"Массив состоит из одного элемента")
