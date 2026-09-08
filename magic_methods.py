# Magic methods = dunder methods (double underscore) __init__, __str__, __eq__
#                 they are automatically called by many of Python's built-in operations.
#                 they allow developers to define or customize the behavior of objects

# class student:

#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa

#     def __str__(self):
#         return f"name: {self.name}, gpa: {self.gpa}"

#     def __eq__(self, other):
#         return self.name == other.name

#     def __gt__(self, other):
#         return self.gpa > other.gpa

# student1 = student("davi", 3.5)
# student2 = student("joão", 3.8)

# print(student1)
# print(student1 == student2)
# print(student1 > student2)

class book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}" 

    def __eq__(self, other):
        return self .title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __lt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"key '{key}' not found"
    
book1 = book("the hobbit", "j.r.r. tolkien", 295)
book2 = book("harry potter", "j.k. rowling", 500)
book3 = book("the lion, the witch and the wardrobe", "c.s. lewis", 208)

# print(book1)
# print(book1 == book2)
# print(book2 < book3)
# print(book2 > book3)
# print(book2 + book3)

# print("lion" in book3)  

print(book1 ['title'])
print(book2 ['author'])
print(book3 ['num_pages'])
print(book1 ['audio'])