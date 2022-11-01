import hashlib

print('Задание 1.')


# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача
# считается не решённой.

string = [i for i in input('Введите предложение латиницей: ').split()]

for i in string:
    print('Хеш-индекс предложения:\n', hashlib.sha1(b'i').hexdigest())


def Hash(string):
    m = []
    for i in string:
        for el, char in enumerate(i):
            m.append(ord(char) - 96)
    return m


coded = Hash(string)

l = []
num = []
for i in string:
    for el in i:
        l.append(el)
    for i in coded:
        num.append(coded.count(i))

print('Количество вхождений в строку каждой буквы:\n', dict(zip(l, num)))