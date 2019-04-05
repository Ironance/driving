country = input('Your nationality: ')
age = input('Your age: ')
age = int(age)
if country == 'Taiwan':
    if age >= 18:
        print('You can attend the driving exam')
    else:
        print('You cannot attend the driving exam')
#elif country == 'America':
