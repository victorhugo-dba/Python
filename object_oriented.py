# object = a "bundle" of related attributes (variables) and methods (functions)
#          ex.: phone, cup, book
#          you need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

class car :
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

car1 = car("Hellcat", 2020, "black", False)
car2 = car("mustang", 2024, "red", True)
car3 = car("corvette", 2025, "blue", True)

# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)

# print(car2.model)
# print(car2.year)
# print(car2.color)
# print(car2.for_sale)

# print(car3.model)
# print(car3.year)
# print(car3.color)
# print(car3.for_sale)

def drive(self):
    print(f"You drive the {self.color} {self.model}")

def stop(self):
    print(f"You stop the {self.color} {self.model}")

def describe(self):
    print(f"{self.year} {self.color} {self.model}")

# drive(car3)
# stop(car1)
describe(car1)