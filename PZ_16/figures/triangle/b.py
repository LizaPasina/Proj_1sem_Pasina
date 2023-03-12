import math

a1 = 7
b1 = 2
c1 = 8
def triangle_perimeter(a = a1, b = b1, c = c1):
    pr = a + b + c
    return(pr)
def triangle_area(a = a1, b = b1, c = c1):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return(s)