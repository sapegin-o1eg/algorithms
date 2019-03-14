"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
from collections import deque


def merge_sort(arr):
    def _merge(left, right):
        sorted_arr = deque()

        while left and right:
            if left[0] < right[0]:
                sorted_arr.append(left.popleft())
            else:
                sorted_arr.append(right.popleft())

        while left:
            sorted_arr.append(left.popleft())

        while right:
            sorted_arr.append(right.popleft())

        return sorted_arr

    len_arr = len(arr)
    if len_arr <= 1:
        return arr

    pivot = len_arr // 2

    left_half = deque()
    right_half = deque()

    for _ in range(len_arr - pivot):
        left_half.appendleft(arr.pop())

    for _ in range(len_arr - (len_arr - pivot)):
        right_half.appendleft(arr.pop())

    return _merge(merge_sort(left_half), merge_sort(right_half))


if __name__ == '__main__':
    import random
    import numpy as np

    SIZE = 5
    MIN_LIMIT = 0
    MAX_LIMIT = np.nextafter(50, 0)

    array = [random.uniform(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
    array_test = sorted(array)

    print(f'Исходный массив:\n{array}')

    result = merge_sort(array)
    result = list(result)
    assert result == array_test, 'Массив не совпадают с образцовым'

    print(f'Отсортированный массив:\n{result}')
