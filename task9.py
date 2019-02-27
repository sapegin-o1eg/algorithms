"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random

MAX_LIMIT = 50
MIN_LIMIT = -50
COLUMNS = 3
ROWS = 3
matrix = [[random.randint(MIN_LIMIT,MAX_LIMIT) for _ in range(COLUMNS)] for _ in range(ROWS)]
column_min = [None] * len(matrix[0])
max_value = None


def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(f"{item:>6}", end='')
        print()


for row in matrix:
    for idx, item in enumerate(row):
        if column_min[idx] is None or column_min[idx] > item:
            column_min[idx] = item

for item in column_min:
    if max_value is None or max_value < item:
        max_value = item

print_matrix(matrix)
print(f"Минимальные элементы столбцов матрицы = {column_min}")
print(f"Максимальный элемент среди минимальных элементов столбцов матрицы = '{max_value}'")