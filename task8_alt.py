"""
Поиск числа, а не цифры
"""

sequence_counter = 0
inputs_quantity = int(input("Введите количество чисел:\n"))
sequence_to_count = int(input("Введите последовательность, которую необходимо найти:\n"))


def count_sequence(number, sequence, counter=0):
    denominator = pow(10, len(str(sequence)))
    if number == 0:
        return counter
    if (number % denominator) == sequence:
        counter += 1
    return count_sequence(number // 10, sequence, counter)


for i in range(1, inputs_quantity+1):
    input_number = int(input(f"Введите {i} число из {inputs_quantity}:\n"))
    sequence_counter += count_sequence(input_number, sequence_to_count)

print(f"В введенных числах последовательность '{sequence_to_count}' встречается {sequence_counter} раз(а)")
