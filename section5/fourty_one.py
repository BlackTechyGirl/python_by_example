name = input('name: ')
num = int(input('num: '))
if num < 10:
    for i in range(num):
        print(name)
else:
    for i in range(3):
        print('too high')