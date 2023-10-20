import math
def f(a, b, c):
    d = b**2 - 4*a*c
    if d>0:
        x1 = (-b + math.sqrt(d)) / 2*a
        x2 = (-b - math.sqrt(d)) / 2*a
        return sorted([x1, x2])
    elif d == 0:
        x = -b/(2*a)
        return [x]
    else:
        return []
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
m = f(a, b, c)
if len(m) == 0:
    print("Уравнение не имеет корней")
else:
    print("Отсортированные корни:", m)
