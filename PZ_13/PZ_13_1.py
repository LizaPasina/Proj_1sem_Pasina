# В матрице элементы кратные 3 увеличить в 3 раза
import random

ch = 0
b = []
while ch < 5:
    a = [random.randint(-15,15) for n in range(1,7)]
    b.append(a)
    ch += 1
print(b)
for i in b:
  if b[i] % 3 == 0:
    b[i] = b[i] * 3
print(b)