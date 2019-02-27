"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
import random

SIZE = 10
MAX_LIMIT = 5
MIN_LIMIT = -5
arr = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]

max_negative = None
max_negative_idx = None

for idx, item in enumerate(arr):
    if item < 0:
        if max_negative is None or max_negative < item:
            max_negative = item
            max_negative_idx = [idx]
        elif item == max_negative:
            max_negative_idx.append(idx)

print(f"Массив: {arr}")
if max_negative is not None:
    print(f"Максимальный отрицательный элемент в массиве: '{max_negative}', на позиции(ях) {max_negative_idx}")
else:
    print(f"В массиве нет отрицательныйх чисел")
