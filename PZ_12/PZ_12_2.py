# Составить генератор (yield), который преобразует все буквенные символы в
# строчные.
def smth(tst):
    yield from [bk.lower() for bk in tst]
tst = str(input("Введите строку:"))
print("Изначальный текст: ", tst)
test = smth(tst)
for i in test:
    print(i)