odd_counter = 0
even_counter = 0


def count(number):
    global odd_counter, even_counter
    if number == 0:
        return
    elif number % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1
    return count(number // 10)


number = int(input("Введие число:\n"))
count(number)
print(f"В числе {number} - {even_counter} четных и {odd_counter} нечетных цифр.")





