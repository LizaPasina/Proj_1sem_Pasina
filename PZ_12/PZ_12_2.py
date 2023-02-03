# Составить генератор (yield), который преобразует все буквенные символы в
# строчные.
def smth(tst):
    yield from [bk.lower() for bk in tst]
tst = 'ThEPРОгрАмС'
print("Изначальный текст: ", tst)
test = smth(tst)
for i in test:
    print(i)