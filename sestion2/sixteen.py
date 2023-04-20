answer = input('is it raining? ')
if answer.lower() == 'yes':
    windy = input('is it windy? ')
    if windy.lower() == 'yes':
        print('it is too windy for an umbrella')
    else:
        print('take an umbrella')
else:
    print('enjoy your day')