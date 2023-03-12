import math

def square_perimeter(a):
    pr = 4 * a
    return pr
def square_area(a):
    s = a ** 2
    return s

a = input("Вы хотите ввести сторону треугольника? ")
if a == "да":
    a = float(input("Введите сторону треугольника: "))
else: a = 7

b = input("Вы хотите ввести сторону треугольника? ")
if b == "да":
    b = float(input("Введите сторону треугольника: "))
else: b = 1

c = input("Вы хотите ввести сторону треугольника? ")
if c == "да":
    c = float(input("Введите сторону треугольника: "))
else: c = 8

print("Периметр треугольника:", triangle_perimeter(a,b,c), "Площадь треугольника:", triangle_area(a,b,c))