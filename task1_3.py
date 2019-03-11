"""
Альтернативнй вариант 2
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random
import sys
from collections import deque

SIZE = 20
MAX_LIMIT = 50
MIN_LIMIT = -50
# arr = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
# arr = deque(arr)
arr = deque([37, -1, -47, 44, -14, -46, -24, 36, -28, 21, -1, 32, 23, 26, 20, 27, -19, -3, 47, 44])

min_idx = max_idx = 0
items_between = deque()
items_sum = 0

print(f"Исходный массив: {arr}")

if len(arr) > 1:
    # обходим массив, находим min и max элементы и их индексы
    for idx in range(len(arr)):
        if arr[idx] > arr[max_idx]:
            max_idx = idx
        if arr[idx] < arr[min_idx]:
            min_idx = idx

    print(f"Минимальный элемент: '{arr[min_idx]}', на позиции {min_idx}")
    print(f"Максимальный элемент: '{arr[max_idx]}', на позиции {max_idx}")

    # если начальный индекс больше конечного, то меняем местами
    if min_idx > max_idx:
        min_idx, max_idx = max_idx, min_idx

    range_start = min_idx+1
    range_end = max_idx

    for i in range(range_start, range_end):
        items_between.append(arr[i])

    # суммируем элементы между min и max лементами исключительно
    for item in items_between:
        items_sum += item

    if (max_idx - min_idx) >= 2:
        print(f"Сумма элементов между min и max = {items_sum}")
    else:
        print(f"min и max элементы находятся рядом")
else:
    print(f"Массив состоит из одного элемента")


# анализ
def check_item(key, value):
    allowed_types = (str, list, dict, tuple, int, float, deque,)
    forbidden_items = (
        key.startswith('__'),
        not isinstance(value, allowed_types)
    )
    if any(forbidden_items):
        return False
    return True


globals_snapshot = {key: value for key, value in globals().items() if check_item(key, value)}


def show_size(obj, verbose=False):
    total_size = 0
    known_ids = set()

    def _count_size(x, level=0):
        _id = id(x)
        if _id in known_ids:
            if verbose:
                print('\t' * level, f'{x} already exists (id={_id}), skipping')
            return 0
        known_ids.add(_id)

        size = sys.getsizeof(x)

        if verbose:
            print('\t' * level, f'level->{level} type={type(x)}. size={size}, obj={x}, id={_id}')

        if hasattr(x, '__iter__'):
            if hasattr(x, 'items'):
                for key, value in x.items():
                    size += _count_size(key, level + 1)
                    size += _count_size(value, level + 1)
            elif not isinstance(x, str):
                for i in x:
                    size += _count_size(i, level + 1)
        return size

    for k, v in obj.items():
        if verbose:
            print(f'\ncalculating var {k}...')
        total_size += _count_size(v)

    return total_size


vars_size = show_size(globals_snapshot)
print(f'\n\nΣ = {vars_size} байт(а)')

"""
Python 3.6.7, x86_64

Исходный массив: deque([37, -1, -47, 44, -14, -46, -24, 36, -28, 21, -1, 32, 23, 26, 20, 27, -19, -3, 47, 44])
Минимальный элемент: '-47', на позиции 2
Максимальный элемент: '47', на позиции 18
Сумма элементов между min и max = 94


Σ = 1992 байт(а)
"""
