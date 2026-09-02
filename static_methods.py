# static methods = a method that belong to a class rather than any object from that class (instance)
#                  usually used for general utility functions

# instance methods = best for operations on instances of the class (objects)
# static methods = best for utility functions that not need access to class data

class employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Team Lead", "Developer", "Intern"]
        return position in valid_positions 


employee1 = employee("John", "Manager")
employee2 = employee("Jane", "team lead")
employee3 = employee("Jack", "developer")

print(employee.is_valid_position("cook"))

print(employee1.info())
print(employee2.info())
print(employee3.info())

