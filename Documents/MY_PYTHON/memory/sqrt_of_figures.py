import math

class SqFigures:
    def __init__(self):
        pass
    def triangle_sq(self, a, b, c):
        # S = (p(p-a)(p-b)(p-c))**0.5
        # где p - полупериметр
        p = (a + b + c)/2
        s = math.sqrt(p*((p - a)*(p - b)*(p - c)))
        return s

    def circle_sq(self, r):
        s = math.pi * r**2
        return s

    def square_sq(self, a, b):
        s = a*b
        return s

if __name__ == '__main__':
    s = SqFigures()

    print(s.circle_sq(2))
    print(s.square_sq(2,8))
    print(s.triangle_sq(4.5,2.8,6.1))