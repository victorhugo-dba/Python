# # keyword arguments = an argument preceded by an indentifier
# #                     helps with readability
# #                     order of arguments dosen't matter
# #                     1. positional 2. default 3. keyword 4. arbitrary

# def hello(greeting, title, first_name, last_name):
#     print(f"{greeting} {title} {first_name} {last_name}")

# hello("Hello", title="Mr.", first_name="João", last_name="Victor")

# for x in range(1, 11):
#     print(x, end=" ")

# print("1", "2", "3", "4", "5", sep="-")

def get_phone(country, area, firts, last):
    return f"{country}-{area}-{firts}-{last}"

phone_num = get_phone(country=61,area=55,firts=92629,last=1235)

print(phone_num)