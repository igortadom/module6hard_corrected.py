from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)
        self.__color = color if self.__is_valid_color(*color) else [0, 0, 0]
        self.filled = False

    def __is_valid_color(self, r, g, b):
        for i in [r, g, b]:
            if isinstance(i, int) and 0 <= i <= 255:
                return [r, g, b]
            else:
                return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        for side in new_sides:
            if len(new_sides) == self.sides_count and isinstance(side, int) and side > 0:
                return len(new_sides)
            else:
                False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self._Figure__sides[0] / (2 * pi)



    def get_square(self):
        return pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        a, b, c = self.get_sides()
        if (a + b > c) and (a + c > b) and (b + c > a):
            pass
        else:
            print(f'Треугольник не существует.')
    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        S = sqrt(p * (p - a) * (p - b) * (p - c))
        if S > 0:
            return S
        else:
            return f'Невозможно вычислить площадь.'


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
        elif len(sides) != self.sides_count:
            sides = [1] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((200, 200, 200), 3, 4, 5)
triangle2 = Triangle((200, 200, 200), 3, 4, 7)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())


cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())


print(len(circle1))
print(cube1.get_volume())
print(triangle1.get_square())
print(triangle2.get_square())

