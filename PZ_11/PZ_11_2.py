# Из предложенного текстового файла (text18-18.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме выведя строки в обратном порядке.

a = 0
t = 0
d = 0
for i in open('text18-18.txt', encoding='UTF-8'):
  print(i, end='')
  t += 1
  while a < 3:
    for j in i:
      if (j == ',') or (j == '.') or (j == '…') or (j == ';') or (j == ':') or (j == '!') or (j == '?') or (j == '—'):
        d = d + 1
        a = a + 1
print(end='\n')

print('Количество строк: ', t, end='\n')
print('Количество знаков препинания : ', d, end='\n')
f1 = open('text18-18.txt', encoding='UTF-8')
l = f1.readlines()
l.reverse()
f1.close()
f2 = open('text18-18_2.txt', 'w')
f2.writelines(l)
f2.close()