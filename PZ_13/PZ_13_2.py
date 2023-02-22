# В матрице найти среднее арифметическое элементов последних двух столбцов.
import random

ch = 0
b = []
while ch < 5:
    a = [random.randint(-15,15) for n in range(1,7)]
    b.append(a)
    ch += 1
print(b)

sort = list(zip(*b))
print("Столбцы :", sort)
j = list(sort[-2:])
ab = [list(map(int, i)) for i in j]
print("Последние 2 столбца:", ab)
sum = 0
a = ab[0]
b = ab[1]
for i in range(len(a)):
  sum = sum + a[i]

sum1 = 0
for i in range(len(b)):
  sum1 = sum1 + b[i]

sum3 = sum1 + sum
f = sum3/(len(a) + len(b))
print("Среднее арифметическое последних 2 столбцов:", f)