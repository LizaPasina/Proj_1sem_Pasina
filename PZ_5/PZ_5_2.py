# Описать функцию PowerA234(A, B, C, D), вычисляющую вторую, третью и
# четвертую степень числа A и возвращающую эти степени соответственно в
# переменные B, C и D (A — входной, B, C, D — выходные параметры; все параметры
# являются вещественными). С помощью этой функции найти вторую, третью и
# четвертую степень пяти данных чисел.
def PowerA234():
    A = input("Введите вещественное число: ")
    while type(A) != float:
        try:
            A = float(A)
        except ValueError:
            print("Введено неправильно")
            A = input("Введите вещественное число: ")
    B = A * A
    C = B * A
    D = C * A
    return A, B, C, D


i = 0
while i < 5:
    A1, B1, C1, D1 = PowerA234()
    print('2 степень числа', A1, 'равна', B1)
    print('3 степень числа', A1, 'равна', C1)
    print('4 степень числа', A1, 'равна', D1)
    i += 1
print('конец')