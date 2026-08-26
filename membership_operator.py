# membership operator = used to test whether a value or variable if found in a sequence 
#                       (string, list, tuple, set or dictionary)
#                       1. in
#                       2. not in

# word = "APPLE"

# letter = input("guess a letter in the secret word: ").upper()

# if letter in word:
#     print(f"there is a {letter}")
# else:
#     print(f"{letter} is not found")

# word = "APPLE"

# letter = input("guess a letter in the secret word: ").upper()

# if letter not in word:
#     print(f"{letter} is not found")
# else:
#     print(f"there is a {letter}")

# students = {"David", "Gabriel", "João"}

# student = input("Enter the name of a student: ").capitalize()

# if student in students:
#     print(f"{student} is a student!")
# else:
#     print(f"{student} is not a student!")

# grades = {"Luan": "A", "Guilherme": "B", "André": "C"}

# student = input("enter a name of a student: ").capitalize()

# if student in grades:
#     print(f"{student} have a grade of {grades[student]}")
# else:
#     print(f"{student} was not found")

email = "fakeemail@gmail.com"

if "@" in email and "." in email:
    print("valid email")
else:
    print("invalid email")