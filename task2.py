"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как
[‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque


def convert_hex_to_dec(num):
    dec_value = 0
    map_hex_to_dec = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    num.reverse()
    num = [map_hex_to_dec[n] for n in num]

    for idx, digit in enumerate(num):
        dec_value += digit * 16 ** idx
    return dec_value


def convert_dec_to_hex(num):
    hexbase = 16
    hex_value = deque()
    map_dec_to_hex = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    while num != 0:
        hex_value.appendleft(map_dec_to_hex[num % hexbase])
        num = num // hexbase
    return hex_value


def print_helper(num):
    return 'Ox' + ''.join(num)


a = input("Введите первое шестнадцатиричное число:\n").upper()
b = input("Введите второе шестнадцатиричное число:\n").upper()

a = deque(a)
b = deque(b)

a = convert_hex_to_dec(a)
b = convert_hex_to_dec(b)

_add = convert_dec_to_hex(a + b)
_mul = convert_dec_to_hex(a * b)

print(f"Сумма = {_add}, произведение = {_mul}")
print(f"Сумма = {print_helper(_add)}")
print(f"Произведение = {print_helper(_mul)}")
