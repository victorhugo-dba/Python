# inheritance = allows a class to inherit attributes and methods from another class
#               helps with code reusability and extensibility
#               class child(parent)

class animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class dog(animal):
    def speak(self):
        print("woof woof!")

class cat(animal):
    def speak(self):
        print("meow mwow!")

class mouse(animal):
    def speak(self):
        print("squeek squeek!")

dog = dog("Scooby")
cat = cat("Garfield")
mouse = mouse("Jerry")

# print(dog.name)
# print(dog.is_alive)
# dog.eat()
# dog.sleep()

# print(cat.name)
# print(cat.is_alive)
# cat.eat()
# cat.sleep()

# print(mouse.name)
# print(mouse.is_alive)
# mouse.eat()
# mouse.sleep()

# dog.speak()
# cat.speak()
# mouse.speak()