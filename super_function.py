# super() = function used in a child class methods from a parent class (superclass).
#           allows you to extend the functionality of the inherited method

class shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"it is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class circle(shape):
    def __init__(self,  color, is_filled, radius):
        super().__init__(color, is_filled)  
        self.radius = radius

    def describe(self):
        super().describe()  # calling the describe method from the parent class
        print(f"it is a circle with an area of {3.14 * self.radius * self.radius}cm^2")

class square(shape):
    def __init__(self,  color, is_filled, width):
        super().__init__(color, is_filled)
        self.side = width

    def describe(self):
        super().describe()
        print(f"it is a square with an area of {self.side * self.side}cm^2")

class triangle(shape):
    def __init__(self,  color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.base = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"it is a triangle with an area of {self.base * self.height / 2}cm^2")

circle = circle(color="red", is_filled=True, radius=5)
square = square(color="blue", is_filled=False, width=6)
triangle = triangle(color="green", is_filled=True, width=7, height=8)

# print(circle.color)
# print(circle.is_filled)
# print(f"Circle radius: {circle.radius}cm")

# print(square.color)
# print(square.is_filled)
# print(f"Square side: {square.side}cm")

# print(triangle.color)
# print(triangle.is_filled)
# print(f"Triangle base: {triangle.base}cm")
# print(f"Triangle height: {triangle.height}cm")

circle.describe()
print(" ")
square.describe()
print(" ")
triangle.describe() 