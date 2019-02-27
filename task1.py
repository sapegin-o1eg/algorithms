"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
"""
for sequence_2_9_item in range(2, 10):
    counter = 0
    for sequence_2_99_item in range(2, 100):
        if sequence_2_99_item % sequence_2_9_item == 0:
            counter += 1
    print(f"Число {sequence_2_9_item} кратно {counter} числу(ам) в последовательности 2..99")
