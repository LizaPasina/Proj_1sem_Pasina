# В матрице элементы кратные 3 увеличить в 3 раза

a = []
tut = int(input("введите кол-во строк матрицы: "))
tam = int(input("введите элементы матрицы: "))
for i in range(tut):
    b = []
    for j in range(tam):
        b.append(j)
    a.append(b)
print(a)