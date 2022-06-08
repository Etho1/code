print('Welcome to the word guessing game!')
magic_word = 'dough'
guess = 'rough'
count = 0
while guess != magic_word:
        guess = input('What is your guess? ')
        count += 1
        if guess != magic_word:
            print('Your guess was not correct.')
        else:
            print('Congratulations! You guessed it!')
            
print(f'It took you {count} guesses. ')