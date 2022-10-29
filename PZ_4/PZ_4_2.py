#Даны целые положительные числа A и B (A < B). Вывести все целые числа от A до
#B включительно; при этом каждое число должно выводиться столько раз, каково его
#значение (например, число 3 выводится 3 раза).
A = input("Введите первое число: ")
while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print("Введено неправильно")
        A = input("Введите первое число: ")
B = input("Введите второе число: ")
while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        print("Введено неправильно")
        B = input("Введите второе число: ")
C = A
while C != 0:
    print(A)
    C = C - 1
while A < B:
    A = A + 1
    C = A
    while C != 0:
        C = C-1
        print(A)