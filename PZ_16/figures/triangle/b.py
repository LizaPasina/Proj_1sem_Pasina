import math

def triangle_perimeter(a,b,c):
    pr = a + b + c
    return pr
def triangle_area(a,b,c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) * 0.5
    return s

a = input("Вы хотите ввести сторону треугольника? ")
if a == "да":
    a = float(input("Введите сторону треугольника: "))
else: a = 7

b = input("Вы хотите ввести сторону треугольника? ")
if b == "да":
    b = float(input("Введите сторону треугольника: "))
else: b = 2

c = input("Вы хотите ввести сторону треугольника? ")
if c == "да":
    c = float(input("Введите сторону треугольника: "))
else: c = 8

print("Периметр треугольника:", triangle_perimeter(a,b,c), "Площадь треугольника:", triangle_area(a,b,c))