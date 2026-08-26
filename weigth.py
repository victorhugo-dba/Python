# phyton weight converter

weight =float(input('enter your weight: '))
unit = input('kilograns or pounds? (k or l) ')

if unit == 'k':
    weight = weight * 2.205
    unit = 'lbs.'
    print(f'your weight is {round(weight, 1)} {unit}')
elif unit == 'l':
    weight = weight / 2.205
    unit = 'kg.'
    print(f'your weight is {round(weight, 1)} {unit}')
else:
    print(f'{unit} is not valid!') 
