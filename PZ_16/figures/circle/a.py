import math

def circle_perimeter(default_radius):
    a = 2 * math.pi * default_radius
    return a
def circle_area(default_radius):
    b = math.pi * default_radius**2
    return b

default_radius = input("Вы хотите ввести радиус? ")
if default_radius == "да":
    default_radius = float(input("Введите радиус: "))
else: default_radius = 5
print("Длина окружности:", circle_perimeter(default_radius), "Площадь окружности:", circle_area(default_radius))