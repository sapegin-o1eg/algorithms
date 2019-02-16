"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""

a = input("Введите первую букву: ")
b = input("Введите вторую букву: ")

a_position = abs(96 - ord(a))
b_position = abs(96 - ord(b))

if a_position == b_position:
    range = 0
else:
    if a_position <  b_position:
        range = b_position - a_position - 1
    else:
        range = a_position - b_position - 1

print(f"Позиция первой буквы = {a_position}\nПозиция второй буквы = {b_position}\nМежду ними {range} символа(ов)")