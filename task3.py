x1 = int(input("Введите x1:"))
y1 = int(input("Введите y1:"))

x2 = int(input("Введите x2:"))
y2 = int(input("Введите y2:"))

if x1 == x2:
    if y1 == y2:
        print("Введенные точки равны.")
        exit(0)
    else:
        print(f"Уравнение прямой для введенных точек: x = {x1}")
        exit(0)
else:
    if y1 == y2:
        print(f"Уравнение прямой для введенных точек: y = {y1}")
        exit(0)
    else:
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2
        print(f"Уравнение прямой для введенных точек: y = {k} x + {b}")
