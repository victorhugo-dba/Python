# class variables = shared among all instances of a class
#                   defined outside the constructor
#                   allow you to share data among all objects created from that class

class student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.num_students += 1

student1 = student("Davi", 29)
student2 = student("joão", 39)
student3 = student("gabriel", 65)
student4 = student("guilherme", 5)

# print(student1.name)
# print(student1.age)

# print(student2.name)
# print(student2.age)
# print(student.class_year)

# print(student.num_students)

print(f"my graduating class of {student.class_year} has {student.num_students}")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)