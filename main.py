import cmath
import math


def quadratic_equation_solve(a, b, c):
    d = b ** 2 - 4 * a * c
    
    if d == 0:
        return
    elif d > 0:
        return [(-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)]
    else:
        return [(-b + cmath.sqrt(d)) / (2 * a), (-b - cmath.sqrt(d)) / (2 * a)]


a = int(input('Введите значение a: '))
b = int(input('Введите значение b: '))
c = int(input('Введите значение c: '))

print(quadratic_equation_solve(a, b, c))