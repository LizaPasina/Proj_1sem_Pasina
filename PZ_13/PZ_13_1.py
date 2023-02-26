# В матрице элементы кратные 3 увеличить в 3 раза
import random

ch = 0
b = []
while ch < 5:
    a = [random.randint(-15,15) for n in range(1,7)]
    b.append(a)
    ch += 1
b1 = []
for i in b:
    a1 = []
    for f in i:
        if f % 3 == 0:
            a1.append(f * 3)
        else:
            a1.append(f)
    b1.append(a1)
print('Изначальная матрица: ', b)
print('Матрица с увеличенными элементами: ', b1)