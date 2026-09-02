# multiple inheritance = inherit from more than one parent class
#                        C(A, B)


# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

class animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class prey(animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class predator(animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class rabbit(prey):
    pass

class hawk(predator):
    pass

class fish(prey, predator):
    pass

rabbit = rabbit("bugs")
hawk = hawk("tony")
fish = fish("nemo")

# rabbit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()

# rabbit.eat()
# rabbit.sleep()
# hawk.eat()
# hawk.sleep()
# fish.eat()
# fish.sleep()