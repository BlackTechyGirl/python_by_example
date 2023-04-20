from django.template.defaultfilters import length

f_name = input('first name: ')
length = len(f_name)

if length < 5:
    surname = input('enter surname: ')
    joined = f_name+surname
    print(joined.upper())
elif length >= 5:
    print(f_name.lower())