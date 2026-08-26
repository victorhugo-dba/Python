unit = input('is this tenperature in Celsius or Fahrenheit? (C/F) ')
temp =float(input('enter the temperature: '))

if unit == 'C':
    temp = round((9 * temp) / 5 + 32, 1)
    print (f'the temperature in Fahrenheit is: {temp} f')
elif unit == 'F':
    temp = round((temp - 32)* 5/9   , 1)
    print (f'the temperature in Celsius is: {temp} c')
else:
    print(f'{unit} is a invalid unit!')