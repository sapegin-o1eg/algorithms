import cProfile


def find_nth_even_eratosthenes(n, max_range=5000):
    sieve = [i for i in range(max_range)]
    sieve[1] = 0

    for i in range(2, max_range):
        if sieve[i] != 0:
            j = i + i
            while j < max_range:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]
    return result[n-1]


def find_nth_even_naive(n, max_range=5000):
    nth_even = None
    nth_even_pos = 0

    for i in range(2, max_range):
        divider = 2
        while i % divider != 0:
            divider += 1
        if divider == i:
            nth_even = i
            nth_even_pos += 1
        if n == nth_even_pos:
            return nth_even

# print(find_nth_even_eratosthenes(500))
# print(find_nth_even_naive(500))
# cProfile.run('find_nth_even_eratosthenes(1000, 10000)')
cProfile.run('find_nth_even_naive(1000, 10000)')


"""
Результаты тестирования find_nth_even_eratosthenes():
    timeit:
    find_nth_even_eratosthenes(10, 10000) - 100 loops, best of 5: 3.89 msec per loop
    find_nth_even_eratosthenes(100, 10000) - 100 loops, best of 5: 3.86 msec per loop
    find_nth_even_eratosthenes(1000, 10000) - 100 loops, best of 5: 3.85 msec per loop

    cProfile.run('find_nth_even_eratosthenes(X, 10000)'):
    1    0.007    0.007    0.009    0.009 task2.py:4(find_nth_even_eratosthenes) - 10
    1    0.007    0.007    0.009    0.009 task2.py:4(find_nth_even_eratosthenes) - 100
    1    0.007    0.007    0.009    0.009 task2.py:4(find_nth_even_eratosthenes) - 1000


Результаты тестирования find_nth_even_naive():
    timeit:
    find_nth_even_naive(10, 10000) - 100 loops, best of 5: 12.2 usec per loop
    find_nth_even_naive(100, 10000) - 100 loops, best of 5: 1.86 msec per loop
    find_nth_even_naive(1000, 10000) - 100 loops, best of 5: 339 msec per loop

    cProfile.run('find_nth_even_naive(X, 10000)'):
    1    0.000    0.000    0.000    0.000 task2.py:19(find_nth_even_naive) - 10
    1    0.003    0.003    0.003    0.003 task2.py:19(find_nth_even_naive) - 100
    1    0.403    0.403    0.403    0.403 task2.py:19(find_nth_even_naive) - 1000
    
Вывод:
    При условии, что тестирование проводитмся с размером изначального массива 10000, алгоритм
    find_nth_even_eratosthenes обладает константной сложностью О(1). Алгоритм наивного перебора обладает ярко
    выраженной нелинейной зависимостью. По мере увеличения индекса искомого простого числа, сложность растет нелинейно.
    Сложность стремится к бесконечности - ярко выраженная асимптота.
"""