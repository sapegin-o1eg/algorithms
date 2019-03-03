"""
    Задание 4 к 3 уроку. Определить, какое число в массиве встречается чаще всего.
    Код обернут в функции для оценки сложности и скорости с помощью timeit и cProfile
"""
import cProfile
import random


def generate_array(size, min_limit, max_max_limit):
    array = [random.randint(min_limit, max_max_limit) for _ in range(size)]
    return array


def print_helper(counter, value):
    if counter > 1:
        print(f"В массиве чаще всего встречается число '{value}', а именно {counter} раз(а)")
    else:
        print("Массив состоит из уникальных элементов")


def most_freq_1(size, min_limit, max_max_limit):
    """Вариант из ПЗ"""

    arr = generate_array(size, min_limit, max_max_limit)

    most_freq_digit = None
    most_freq_digit_count = None

    for item in arr:
        counter = 0
        for digit in arr:
            if item == digit:
                counter += 1
        if most_freq_digit is None or counter > most_freq_digit_count:
            most_freq_digit = item
            most_freq_digit_count = counter

    print_helper(most_freq_digit_count, most_freq_digit)


def most_freq_2(size, min_limit, max_max_limit):
    """Альтернативнй вариант 1"""

    arr = generate_array(size, min_limit, max_max_limit)

    array_stats = dict()
    most_freq = {'digit': None,
                 'count': None}

    for item in arr:
        array_stats[item] = array_stats.get(item, 0) + 1
        if most_freq['digit'] is None or array_stats[item] > most_freq['count']:
            most_freq['digit'] = item
            most_freq['count'] = array_stats[item]

    print_helper(most_freq['count'], most_freq['digit'])


def most_freq_3(size, min_limit, max_max_limit):
    """Альтернативнй вариант 2"""

    arr = generate_array(size, min_limit, max_max_limit)
    most_freq_value = None
    most_freq_count = None

    for i in set(arr):
        i_count = arr.count(i)
        if most_freq_value is None or i_count > most_freq_count:
            most_freq_value = i
            most_freq_count = i_count

    print_helper(most_freq_count, most_freq_value)


# cProfile.run('most_freq_3(20000, -50, 50)')
# most_freq_3(5, 1, 2)

"""
Результаты тестирования most_freq_1 (Вариант из ПЗ):
    timeit:
    most_freq_2(10, -50, 50) - 100 loops, best of 3: 38.5 usec per loop
    most_freq_2(20, -50, 50) - 100 loops, best of 3: 83.3 usec per loop
    most_freq_2(200, -50, 50) - 100 loops, best of 3: 1.76 msec per loop
    most_freq_2(2000, -50, 50) - 100 loops, best of 3: 133 msec per loop

    cProfile.run('most_freq_1(X, -50, 50)'):
    1    0.000    0.000    0.000    0.000 task1.py:15(most_freq_1)- 20
    1    0.002    0.002    0.003    0.003 task1.py:15(most_freq_1) - 200
    1    0.143    0.143    0.148    0.148 task1.py:15(most_freq_1) - 2000


    Видна нелинейная зависимость. Сложность алгоритма О(n^2) из-за вложенного цикла в другой цикл.
    Количество итераций будет равно количеству элементов входного массива во второй степени.
    Алгоритм менее расточителен к памяти, но более требователен к процессорному времени.
    С большой размерностью входного массива алгоритм будет работать очень долго.


Результаты тестирования most_freq_2 (Альтернативнй вариант 1):
    timeit:
    most_freq_2(10, -50, 50) - 100 loops, best of 3: 42.2 usec per loop
    most_freq_2(20, -50, 50) - 100 loops, best of 3: 63 usec per loop
    most_freq_2(200, -50, 50) - 100 loops, best of 3: 428 usec per loop
    most_freq_2(2000, -50, 50) - 100 loops, best of 3: 3.58 msec per loop
    most_freq_2(20000, -50, 50) - 100 loops, best of 3: 33.1 msec per loop

    cProfile.run('most_freq_2(X, -50, 50)'):
    1    0.000    0.000    0.000    0.000 task1.py:72(most_freq_2) - 20
    1    0.000    0.000    0.001    0.001 task1.py:72(most_freq_2) - 200
    1    0.001    0.001    0.009    0.009 task1.py:72(most_freq_2) - 2000
    1    0.006    0.006    0.054    0.054 task1.py:72(most_freq_2) - 20000

    Самый быстрый вариант. Видна линейная зависимость. Сложность алгоритма О(n)
    Алгоритм более требователен к памяти, т.к. создает словарь с промежуточными данными.
    Размер словаря будет равен числу уникальных элементов во входном массиве.
    Быстро справляется с большим массивом на входе, из-за того что однопроходной.
    Количество итераций равно размеру входного массива


Результаты тестирования most_freq_3 (Альтернативнй вариант 2):
    timeit:
    most_freq_3(10, -50, 50) - 100 loops, best of 3: 37.1 usec per loop
    most_freq_3(20, -50, 50) - 100 loops, best of 3: 57.9 usec per loop
    most_freq_3(200, -50, 50) - 100 loops, best of 3: 627 usec per loop
    most_freq_3(2000, -50, 50) - 100 loops, best of 3: 6.6 msec per loop
    most_freq_3(20000, -50, 50) - 100 loops, best of 3: 63.2 msec per loop

    cProfile.run('most_freq_3(X, -50, 50)'):
    1    0.000    0.000    0.000    0.000 task1.py:98(most_freq_3) - 10
    1    0.000    0.000    0.000    0.000 task1.py:98(most_freq_3) - 20
    1    0.000    0.000    0.001    0.001 task1.py:98(most_freq_3) - 200
    1    0.000    0.000    0.008    0.008 task1.py:98(most_freq_3) - 2000
    1    0.001    0.001    0.087    0.087 task1.py:98(most_freq_3) - 20000

    Неожиданный результат. Видна линейная зависимость. Хотя, на первый взгляд, ожидал O(2n^2)
    Видно, что разработчики Python постарались реализовать встроенные функции наилучшим образом.
    Похоже, что arr.count() выполняется 1 раз, кешируя данные для дальнейшего использования
    в последующих итерациях цикла for. Я предполагаю, что сложность алгоритма O(3n)

Вывод:
    Чаще всего задачу можно решить ресколькими способами. При написании кода необходимо выбирать
    те пути решения, которые подходят для конкретной задачи. Необходимо опираться на требуемую скорость выполнения,
    доступные ресурсы, перспективы использования кода в будущем. Иногда, жертвуя оперативной памятью, можно написать
    быстрый алгоритм. Или, если памяти мало, можно использовать более медленный алгоритм, но необходимо учитывать
    асимптотическую сложность, иначе код будет выполняться бесконечно долго.
    Также стало приятным сюрпризом, как быстро работают встроенные классы и их методы.
"""
