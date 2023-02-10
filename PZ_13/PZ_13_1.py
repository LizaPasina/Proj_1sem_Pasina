# В матрице элементы кратные 3 увеличить в 3 раза
import random

ch = 0
b = []
while ch < 5:
    a = [random.randint(-15,15) for n in range(random.randint(1,7))]
    b.append(a)
    ch += 1
print(b)
# s = [f for f in b if f % 3 == 0]
s = []
for i in b:
    s.append(b[i] % 3 == 0)
print(s)
