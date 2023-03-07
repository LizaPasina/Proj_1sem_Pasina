# Из исходного текстового файла (expansion.txt) выбрать имена фалов,
# соответствующие типам: .xls, .xml, .html, .css, .py.Посчитать количество полученных
# элементов.
import re

f = open('expansion.txt', encoding="utf8")
count = 0
for i in f:
    p = re.findall(r'\.xls|.xml|.html|.css|.py', i)
    if len(p) > 0:
        count += 1
        print(i)
print('Количество элементов:', count)