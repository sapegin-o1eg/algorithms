digit_counter = 0
inputs_quantity = int(input("Введите количество чисел:\n"))
digit_to_count = int(input("Введите цифру, которую необходимо найти:\n"))


def count_digit(number, digit, counter=0):
    if number == 0:
        return counter
    if (number % 10) == digit:
        counter += 1
    return count_digit(number // 10, digit, counter)


for i in range(1, inputs_quantity+1):
    input_number = int(input(f"Введите {i} число из {inputs_quantity}:\n"))
    digit_counter += count_digit(input_number, digit_to_count)

print(f"В введенных числах цифра '{digit_to_count}' встречается {digit_counter} раз(а)")
