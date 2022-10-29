# Даны три числа. Найти среднее из них (число расположенное между наименьшим и наибольшим)
a,b,c = input('Введите 1-ое число: '), input('Введите 2-ое число: '), input('Введите 3-ое число: ')
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Неправильно')
        a = input('Введите 1-ое число: ')
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Неправильно')
        b = input('Введите 2-ое число: ')
while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print('Неправильно')
        c = input('Введите 3-ое число: ')
if (b < a < c) or (c < a < b):
    print('Среднее', a)
elif (a < b < c) or (c < b < a): print('Среднее', b)
else:
    print('Среднее', c)