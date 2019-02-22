input_number = int(input("Введите число:\n"))


def invert(number, result=''):
    if number == 0:
        return result
    new_number = number // 10
    new_result = result + str(number % 10)
    return invert(new_number, new_result)


flipped_number = invert(input_number)
print(f"Число {input_number} в обратном порядке = {flipped_number}")