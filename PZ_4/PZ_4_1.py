#Дано вещественное число X и целое число N (> 0). Найти значение выражения 1 + X + X^2/(2!) +...+ X^N/(N!) (N! = 1 * 2 ...N).
# Полученное число является приближенным значением функции exp в точке X.
X = input("Введите вещественное число X: ")
while type(X) != float:
    try:
        X = float(X)
    except ValueError:
        print("Введено неправильно")
        X = input("Введите вещественное число X: ")
N = input("Введите целое число N: ")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Введено неправильно")
        N = input("Введите целое число N: ")
a = 1
b = 1
e = 1
factorial = 1
while a <= N:
    while e <= a:
        factorial = factorial * e
        e += 1
    b = b + ((X ** a)/factorial)
    a += 1
print("Приближенное значение функции exp в точке X", b)