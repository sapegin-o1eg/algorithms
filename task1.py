"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""


def bubble_sort_enhanced(arr):
    arr_len = len(arr)

    while arr_len > 1:
        sorted_ = True
        for i in range(-1, -1 * arr_len, -1):
            if arr[i] > arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                sorted_ = False
        if sorted_:
            return

        arr_len -= 1


if __name__ == '__main__':
    import random

    SIZE = 5
    MIN_LIMIT = -100
    MAX_LIMIT = 99

    array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
    random.shuffle(array)
    array_test = sorted(array, reverse=True)

    print(f'Исходный массив:\n{array}')

    bubble_sort_enhanced(array)
    assert array == array_test, 'Массив не совпадает с образцовым'

    print(f'Отсортированный массив:\n{array}')
