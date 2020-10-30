"""
2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
from collections import Counter, deque


class MyNode:
    """Класс для создания дерева"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.table = dict()

    def get_table(self, root, path=''):
        """Метод для получения таблицы Хаффмана"""
        if root.left is None and root.right is None:
            self.table[root.value] = path
        if root.left:
            self.get_table(root.left, path=path + '0')
        if root.right:
            self.get_table(root.right, path=path + '1')

        return self.table


string = 'beep boop beer!'

print(f'Исходная строка: "{string}"')

array = Counter(string)

array = deque(sorted(array.items(), key=lambda x: x[1]))

print('*' * 50)
print(f'Таблица частот:')
for char, freq in array:
    print(f'"{char}"\t\t{freq}')

counter_ = 0
while len(array) != 1:
    a = array.popleft()
    b = array.popleft()

    a_value = a[1] if isinstance(a, tuple) else a.value
    b_value = b[1] if isinstance(b, tuple) else b.value

    root = MyNode(a_value + b_value)
    root.left = MyNode(a[0]) if isinstance(a, tuple) else a
    root.right = MyNode(b[0]) if isinstance(b, tuple) else b

    idx = 0
    len_ = len(array)

    while idx < len_:
        value = array[idx][1] if isinstance(array[idx], tuple) else array[idx].value
        if root.value <= value:
            array.insert(idx, root)
            break
        idx += 1
    else:
        array.append(root)

    counter_ += 1

tree = array[0]
table = tree.get_table(tree)

print('*' * 50)
print('Таблица Хаффмана')
for char, code in table.items():
    print(f'"{char}"\t\t{code}')

print('*' * 50)
print(f'Закодированная строка "{string}":')
for i in string:
    print(f'{table[i]}', end=' ')
