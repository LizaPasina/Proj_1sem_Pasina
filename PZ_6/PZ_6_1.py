# Дан целочисленный список A размера 10. Вывести порядковый номер последнего из
# тех его элементов AK, которые удовлетворяют двойному неравенству A1 < AK < A10.
# Если таких элементов нет, то вывести 0.

N = 10
i = 0
A = []
print("Количество элементов в списке:", N)
while i < 10:
    A.append(int(input('Введите элемент: ')))
    i += 1
print("Список:", A)
K = 0
T = 8
for i in range(1, N-1):
    if (A[0] < A[i]) and (A[i] < A[9]):
        K = i
    else:
        T =- 1
if T <= 0:
    print(0)
else:
    print('Порядковый номер:', K + 1)