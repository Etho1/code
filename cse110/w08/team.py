word1 = 'commitment'
capital = input('What is your favorite letter? ')
for letter in word1:
    if letter == capital:
        # print(letter.upper(),end='')
        print('_',end='')
    else:
        print(letter,end='')