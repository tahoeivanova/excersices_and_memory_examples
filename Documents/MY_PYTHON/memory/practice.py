# Найти площадь и периметр прямоугольного треугольника по двум заданным катетам.

class Triangle:
    __slots__ = ('x', 'y')
    # два катета
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Площадь треугольника равна половине площади прямоуглоьника, сторонами которого являются катеты.
    def square(self):
        return self.x * self.y / 2

    # Периметр - сложение всех сторон треугольника.
    def perimeter(self):
        # Найдем гипотенузу.
        c = (self.x**2 + self.y**2)**0.5
        return c + self.x + self.y

if __name__ == '__main__':
    triangle = Triangle(1,2)
    print(triangle.square())
    print(round(triangle.perimeter(),2))
