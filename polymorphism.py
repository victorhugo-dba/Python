# polymorphism = greek word that means to "have many forms of faces"
#                poly = many
#                morphe = form

#                two ways to achieve polymorphism 
#                1. inheritance = an object could be treated of the same type as a parent class
#                2. "duck typing" = object must have necessary attributes/methods

from abc import abstractmethod


class shape:

    @abstractmethod
    def area (self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class square(shape):
    def __init__(self, side):
        self.width = side 

    def area(self):
        return self.width ** 2

class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


class pizza(circle):
    def __init__(self, toppings, radius):
        super().__init__(radius)
        self.toppings = toppings


shapes = [circle(4), square(5), triangle(6, 7), pizza(["pepperoni"], 15)]

for shape in shapes:
    print(f"{shape.area()}cm^2")