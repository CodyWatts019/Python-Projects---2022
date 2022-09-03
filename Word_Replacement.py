def replace_word():
    str = 'Hey I am Alex and she is XYZ'
    word_to_replace = input('Enter the word you want to replace: ')
    replaced_word = input('Enter the replacement word: ')
    print(str.replace(word_to_replace,replaced_word))

replace_word()

def replace_value():
    a = 25
    b = 23
    c = a-b
    age = c
    print('Our age difference is ',age, 'years.')

replace_value()