action = "do"
result = None
error = None


def dispatch():
    act = "do"
    res = None
    err = None

    operator = input("Введите операцию - '+', '-', '*', '/'; '0' - выход:\n")

    if operator == "0":
        act = "exit"
        err = "Завершение программы..."
        return act, err, res
    elif operator != "+" and operator != "-" and operator != "*" and operator != "/":
        err = "Введена недопустимая операция."
        return act, err, res

    a = int(input(f"Введите первый операнд (a {operator} b) a="))
    b = int(input(f"Введите второй операнд ({a} {operator} b) b="))

    if operator == "+":
        res = f"{a} {operator} {b} = {a + b}"
    elif operator == "-":
        res = f"{a} {operator} {b} = {a - b}"
    elif operator == "*":
        res = f"{a} {operator} {b} = {a * b}"
    elif operator == "/" and b == 0:
        err = "Ошибка! Деление на ноль."
    elif operator == "/":
        res = f"{a} {operator} {b} = {a / b}"

    return act, err, res


while action == "do":
    action, error, result = dispatch()
    if error:
        print(error)
    else:
        print(result)

