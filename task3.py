"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

SIZE = 5
MAX_LIMIT = 50
MIN_LIMIT = -50
arr = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]

min_idx = None
max_idx = None
min_item = None
max_item = None

print(f"Исходный Массив:\n{arr}")

for idx, item in enumerate(arr):
    if min_item is None or min_item > item:
        min_item = item
        min_idx = idx
    elif max_item is None or max_item < item:
        max_item = item
        max_idx = idx

arr[max_idx], arr[min_idx] = arr[min_idx], arr[max_idx]

print(f"Максимальный элемент = {max_item} на позиции {max_idx}")
print(f"Минимальный элемент = {min_item} на позиции {min_idx}")
print(f"Массив после обмена местамии min и max элементов:\n{arr}")