"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком
сложно, то используйте метод сортировки, который не рассматривался на уроках
"""


def get_median(arr):
    min_item = None
    max_item = None
    counter = dict()
    sum_ = 0
    len_ = 0

    for item in arr:
        if min_item is None or item < min_item:
            min_item = item
        if max_item is None or item > max_item:
            max_item = item
        counter[item] = counter.get(item, 0) + 1
        len_ += 1

    position = (len_ + 1) / 2

    for i in range(min_item, max_item + 1):
        if counter.get(i, 0):
            sum_ += counter[i]
            if sum_ >= position:
                return i


if __name__ == '__main__':
    import random
    from numpy import median

    SIZE = 2
    MIN_LIMIT = 0
    MAX_LIMIT = 10
    array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(2 * SIZE + 1)]

    my_median = get_median(array)
    assert median(array) == my_median, 'Значение не соответствует медиане'

    print(f'Исходный массив:\n{array}')
    print(f'Медиана:\n{my_median}')
