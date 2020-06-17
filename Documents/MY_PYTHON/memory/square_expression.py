# Найти корни квадратного уравнения
# a*x^2 + b*x + c = 0
# D = b**2 - 4*a*c
# D>0 - два корня, D=0 - один корень, D<0 - нет корней
# x_1, x_2 = (-b +- D ** 0.5)/2*a

import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

D = b**2 - 4*a*c
print(D)
if D > 0:
    x_1 = (-b + math.sqrt(D))/(2*a)
    x_2 = (-b - math.sqrt(D))/(2*a)
    print(f'{x_1}, {x_2}')

elif D == 0:
    x_1 = -b / (2 * a)
    print(f'{x_1}')

else:
    print('Нет корней')