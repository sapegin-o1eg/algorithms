import random

begin_int = int(input("Введите начало для диапазона целых чисел:"))
end_int = int(input("Введите конец для диапазона целых чисел:"))

begin_float = float(input("Введите начало для диапазона вещ. чисел: "))
end_float = float(input("Введите конец для диапазона вещ. чисел: "))

begin_char = ord(input("Введите начало для диапазона символов (a-z): "))
end_char = ord(input("Введите конец для диапазона символов (a-z): "))

result = random.randint(begin_int, end_int)
print(f"Случайное число для диапазона целых чисел = {result}")

result = random.uniform(begin_float, end_float)
print(f"Случайное число для диапазона вещ. чисел = {result}")

if begin_char == end_char:
    print(f"Случайный символ для диапазона символов = {chr(begin_char)}")
    exit(0)
else:
    result = chr(random.randint(begin_char, end_char))
    print(f"Случайный символ для диапазона символов = {result}")
