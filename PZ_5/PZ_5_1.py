#Составить программу, в которой функция генерирует четырехзначное число и определяет, есть ли в числе одинакове цифры.
from random import randint
num = randint(1000, 9999)


def nums():
    b = num // 1000
    c = (num % 1000) // 100
    d = (num % 100) // 10
    e = (num % 100) % 10
    if (b == c) or (b == d) or (b == e) or (c == d) or (c == e):
        print('есть одинаковые цифры')
    else: print('нет одинаковых цифр')


print('В четырехзначном числе', num)
nums()