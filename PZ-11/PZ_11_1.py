# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Среднее арифметическое элементов:
# Последовательность, в которой каждый последующий элемент равен квадрату суммы двух
# соседних элементов:


A = ['-23 3 -21 34 11 -5 8']
f3 = open('data_3.txt', 'w')
f3.writelines(A)
f3.close()

f4 = open('data_4.txt', 'w')
f4.write('Исходные данные: ')
f4.write('\n')
f4.writelines(A)
f4.close()

f3 = open('data_3.txt')
k = f3.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()

f3 = open('data_3.txt', 'a')
sum = 0
for i in range(len(k)):
    sum = sum + k[i]
sum = sum/len(k)

f4 = open('data_4.txt', 'a')
f4.write('\n')
print('Количество элементов: ', len(k), file=f4)
f4.close()

f4 = open('data_4.txt', 'a')
f4.write('\n')
print('Cреднее арифметическое ', sum, file=f4)
B = []
Kv = 0
n = 0
f3 = open('data_3.txt')
for i in range(len(k)):
    if i == 0:
        Kv = (k[i + 1])**2
        B.append(Kv)
    elif i == len(k)-1:
        Kv = (k[i - 1])**2
        B.append(Kv)
    else:
        Kv = (k[i-1]+k[i+1])**2
        B.append(Kv)
f4 = open('data_4.txt', 'a')
f4.write('\n')
print('Последовательность, в которой каждый последующий элемент равен '
      'квадрату суммы двух соседних элементов', B, file=f4)
f4.close()