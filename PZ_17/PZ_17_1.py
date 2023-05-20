# Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления
# площади, длины окружности и диаметра.

class Krug:
   def __init__(self,radius):
       self.radius = radius

   def get_r(self):
       return self.radius

   def pl(self):
       return 3.14 * (self.radius ** 2)

   def dlina(self):
       return 2 * 3.14 * self.radius

   def diameter(self):
       return 2 * self.radius

k = Krug(5)
print("Радиус:",k.get_r())
print("Площадь:",k.pl())
print("Длина:",k.dlina())
print("Диаметр:",k.diameter())
