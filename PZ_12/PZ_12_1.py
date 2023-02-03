# В последовательности на n целых элементов найти произведение элементов
# средней трети.
import random
from functools import reduce

n = int(input("Введите кол-во элементов кратное 3: "))
while n%3 != 0:
  print('Неправильно')
  n = int(input("Введите кол-во элементов кратное 3: "))

spsk = []
ch = 3
i = 0
while i < n:
    spsk.append(random.randint(-10,10))
    i += 1
print("Список: ",spsk)
a = int(len(spsk)/ch)
b = a
spsk1 = []
for i in spsk:
    while b < a*2:
        spsk1.append(spsk[b])
        b = b + 1
print('Средняя треть:', spsk1)
c = reduce(lambda x,y: x*y, spsk1)
print('Произведение средней трети:', c)
