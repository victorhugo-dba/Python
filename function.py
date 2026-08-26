# function = a block of reusable code 
# place () after the function name to invoke it

# def happy_birthday(name,):
#     print(f"happy birthday to {name}")
#     print("have a happy life")
#     print("happy birthday to you")
#     print()

# happy_birthday("bro")
# happy_birthday("steve")
# happy_birthday("mike")

# def happy_birthday(name, age):
#     print(f"happy birthday to {name}")
#     print(f"happy {age} years of life")
#     print("happy birthday to you")
#     print()

# happy_birthday("bro", 20)
# happy_birthday("steve", 35)
# happy_birthday("mike", 42)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount} is due: {due_date}")

# display_invoice("robervalc", 42.000, "01/03") 


# return = statment used to end a function
# and send a result back to the caller

# def add (x, y):
#     z = x + y
#     return z

# def sub (x, y):
#     z = x - y
#     return z

# def multi(x, y):
#     z = x * y
#     return z

# def divide(x, y):
#     z = x / y
#     return z

# # print(add(1, 2 ))
# # print(sub(1, 2 ))
# # print(multi(1, 2 ))
# print(divide(1, 2 ))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("victor", "hugo")

print(full_name)