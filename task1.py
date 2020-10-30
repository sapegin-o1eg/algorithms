"""
1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
"""


def count_substrings(string):
    """Возвращает кол-во подстрок в строке"""
    subs_seen = list()
    subs_counter = 0
    len_ = len(string)

    for left_slice in range(len_):
        left = left_slice + 1
        right = len_ + 1 if subs_seen else len_
        for right_slice in range(left, right):
            hash_ = hash(string[left_slice:right_slice].encode())
            if hash_ not in subs_seen:
                subs_seen.append(hash_)
                subs_counter += 1

    return subs_counter


if __name__ == '__main__':
    s = input(f'Введите строку:\n')
    c = count_substrings(s)
    print(f'В введенной строке {c} подстрок')
