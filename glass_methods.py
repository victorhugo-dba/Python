# Glass methods = allow operations related to the class itself
#                 take (cls) as the first parameter, which represents the class itself

class student:

    count = 0
    total_gpa = 0.0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        student.count += 1
        student.total_gpa += gpa

    def get_info(self):
        return f"Name: {self.name} GPA: {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_average_goa(cls):
        if cls.count == 0:
            return 0.0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"

student1 = student("davi", 2.0)
student2 = student("joão", 3.8)
student3 = student("maria", 4.0)

print(student.get_count())
