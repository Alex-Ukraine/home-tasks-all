class Rectangle:
    def __init__(self, a=4, b=3):
        if type(a) not in (float, int) or type(b) not in (float, int):
            raise ValueError
        if a <= 0 or b <= 0:
            raise ValueError
        self.__side_a = float(a)
        self.__side_b = float(b)

    def get_side_a(self):
        return self.__side_a

    def get_side_b(self):
        return self.__side_b

    def area(self):
        return self.__side_a * self.__side_b

    def perimeter(self):
        return (self.__side_a + self.__side_b) * 2

    def is_square(self):
        return self.__side_a == self.__side_b

    def replace_sides(self):
        self.__side_a, self.__side_b = self.__side_b, self.__side_a


class ArrayRectangles:
    def __init__(self, *args, n=0):
        self.__rectangle_array = []

        for rect in args:
            if isinstance(rect, Rectangle) or rect is None:
                self.__rectangle_array.append(rect)
            elif isinstance(rect, list):
                for x in rect:
                    self.__rectangle_array.append(x)

        if n > len(self.__rectangle_array):
            self.__rectangle_array.extend([None] * (n - len(args)))

    def add_rectangle(self, some=Rectangle()):
        for index, x in enumerate(self.__rectangle_array):
            if x is None:
                self.__rectangle_array[index] = some
                return True
        return False

    def number_max_area(self):
        max = self.__rectangle_array[0].area()
        imax = 0
        for index, x in enumerate(self.__rectangle_array):
            if isinstance(x, Rectangle) and x.area() > max:
                max = x.area()
                imax = index
        return imax

    def number_min_perimeter(self):
        min = self.__rectangle_array[0].perimeter()
        imin = 0
        for index, x in enumerate(self.__rectangle_array):
            if isinstance(x, Rectangle) and x.perimeter() < min:
                min = x.perimeter()
                imin = index
        return imin

    def number_square(self):
        return sum(
            bool(isinstance(x, Rectangle) and x.is_square())
            for x in self.__rectangle_array
        )
