word = input('enter a word: ')
first = word[0]
rest = word[1:]
if first == 'a' and first == 'e' and first == 'i' and first == 'o' and first == 'u':
    new_word = word + 'way'
else:
    new_word = rest+first+'ay'
print(new_word.lower())