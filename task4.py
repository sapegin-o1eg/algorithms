"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random

SIZE = 5
MAX_LIMIT = 5
MIN_LIMIT = 0
arr = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]

most_freq_digit = None
most_freq_digit_count = None

print(arr)

for item in arr:
    counter = 0
    for digit in arr:
        if item == digit:
            counter += 1
    if most_freq_digit is None or counter > most_freq_digit_count:
        most_freq_digit = item
        most_freq_digit_count = counter

if most_freq_digit_count > 1:
    print(f"В массиве чаще всего встречается число '{most_freq_digit}', а именно {most_freq_digit_count} раз(а)")
else:
    print("Массив состоит из уникальных элементов")
