display = int(input(''''
1 ) Square
2 ) Triangle

Enter a number: 
'''))
if display == 1:
    length = int(input('What is the length of one of its sides? '))
    area = length**2
    print(area)
elif display == 2:
    base = int(input('What is the base of the triangle? '))
    height = int(input('What is the height of the triangle? '))
    area = (base*height)/2
    print(area)
else:
    print('Sorry, wrong input')