# phyton calculator

operator = input('enter an operator (+ - * /): ')
num1 = float(input ('enter the firts number:'))
num2 = float(input ('enter the second number:'))

# print(num1 + num2)
# if operator == '+':
#     result = num1 + num2
#     print(result)
# elif operator == '-':
#     result = num1 - num2
#     print(result)
# elif operator == '*':
#     result = num1 * num2
#     print(result)
# elif operator == '/':
#     result = num1 / num2
#     print(result)

if operator == '+':
    result = num1 + num2
    print(round(result, 3))
elif operator == '-':
    result = num1 - num2
    print(round(result, 3  ))
elif operator == '*':
    result = num1 * num2
    print(round(result, 3))
elif operator == '/':
    result = num1 / num2
    print(round(result, 3))
else:
    print(f'{operator} is not valid operator!')