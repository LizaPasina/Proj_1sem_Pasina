# Дан список размера N, все элементы которого, кроме первого, упорядочены по
# возрастанию. Сделать список упорядоченным, переместив первый элемент на новую
# позицию.
import random

N = input("Введите размер списка: ")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Нужно ввести целое число')
        N = input('Введите размер списка: ')

A = []
b = 0
while b < N:
    A.append(random.randint(-10, 10))
    b += 1
A.sort(key=None, reverse=False)
A.insert(0,random.randint(-10, 10))
print("Список:", A)
d = A.pop(0)
A.append(d)
A.sort(key=None, reverse=False)
print("Упорядоченный список:", A)