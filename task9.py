input_number = None
prev_summ = 0
max_summ = 0
max_number = 0


def add_all_digits(number, summ=0):
    if number == 0:
        return summ
    summ += number % 10
    return add_all_digits(number // 10, summ)


while input_number != 0:
    input_number = int(input("Введите число:"))
    prev_summ = add_all_digits(input_number)
    if prev_summ > max_summ:
        max_summ = prev_summ
        max_number = input_number

print(f"Максимальная сумма цифр = {max_summ} у введенного числа {max_number}")
