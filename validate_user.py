# validate user input exercise
# 1 username is no more than 12 charecters 
# 2 username must not contain spaces
# 3 username must not contain digits  

username = input ('enter your username: ')

username.find(" ")

username.isalpha()

if len(username) > 12:
    print("your username can't be more than 12 characters ")
elif not username.find(" ") == -1:
    print("your username can't contain spaces")
elif not username.isalpha():
    print("your username can't contain numbers")
else:
    print(f"welcome {username}")