def calculate_summ(n, nth_element=-2, summ=0):
    if n == 0:
        return summ
    nth_element *= -0.5
    summ += nth_element
    return calculate_summ(n-1, nth_element, summ)


print("Дана последовательность 1, -0.5, 0.25, -0.125 ...")
n = int(input("Сумму какого количества элементов необходимо найти?:\n"))
result = calculate_summ(n)
print(f"Сумма {n} элементов последовательности = {result}")