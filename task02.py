# сделай класс треугольника, в нем конструктор принимает три стороны и сохраняет их себе,
# а также есть функция, возвращающая площадь этого треугольника.
# Для демонстрации, создай несколько треугольников и напечатай их площади
import numbers

class Triangle(object):
    def __init__(self, first_side, second_side, third_side):
        if not all([isinstance(x, numbers.Number) for x in [first_side, second_side, third_side]]):
            raise Exception('Triangle sides must be numbers: ({0},{1},{2})'.format(first_side, second_side, third_side))

        triangle = [first_side, second_side, third_side]
        triangle = sorted(triangle)
        if triangle[0] + triangle[1] <= triangle[2]:
            raise Exception('This triangle ({0},{1},{2}) does not exist'.format(first_side, second_side, third_side))

        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    def calculation_of_area(self):
        semiperimeter = (self.first_side + self.second_side + self.third_side) / 2
        self.area = (semiperimeter * (semiperimeter - self.first_side) * (semiperimeter - self.second_side) * (semiperimeter - self.third_side))**0.5
        return self.area

    def calculation_of_perimeter(self):
        self.perimeter = self.first_side + self.second_side + self.third_side
        return self.perimeter


try:
    d = Triangle(0.5, 2, 3)
    print(d.calculation_of_area())
except Exception as e:
    print(e)

try:
    f = Triangle(-99, 2, 3)
    print(f.calculation_of_area())
except Exception as e:
    print(e)

try:
    g = Triangle(-3, -4, -5)
    print(g.calculation_of_area())
except Exception as e:
    print(e)

try:
    h = Triangle('3', '4', '5')
    print(h.calculation_of_area())
except Exception as e:
    print(e)

try:
    a = Triangle(3, 4, 5)
    print(a.calculation_of_area())
except Exception as e:
    print(e)

try:
    b = Triangle(1, 2, 3)
    print(b.calculation_of_area())
except Exception as e:
    print(e)

try:
    c = Triangle(15, 15, 15)
    print(c.calculation_of_area())
except Exception as e:
    print(e)

try:
    print(a.calculation_of_area() + b.calculation_of_area() + c.calculation_of_area())
except Exception as e:
    print(e)

