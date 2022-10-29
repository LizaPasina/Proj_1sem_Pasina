a = input('Введите целое трехзначное число: ')
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('неправильно')
        a = input('Введите целое трехзначное число: ')
e = a // 100 #единицы
c = ((a // 10) % 10) * 100 #сотни
d = (a % 10) * 10 #десятки
a = c + d + e
print(a)
