# 'duck typing' = another way to achieve polymorphism besides inheritance
#                 object must have the minimum necessary attributes/methods
#                 "if it looks like a duck and quacks like a duck, it must be a duck."

class animal:
    alive = True

class dog(animal):
    def speak(self):
        return "woof woof!"

class cat(animal):
    def speak(self):
        return "meow mwow!"

class car:

    alive = False

    def speak(self):
        print("honk!")

animals = [dog(), cat(), car()]

for animal in animals:
    print(animal.speak())
    print(animal.alive)