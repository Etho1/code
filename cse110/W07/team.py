import random
replay = 'yes'
while replay == 'yes':
    magic_number = random.randint(1,100)
    guess = -1
    count = 0
    while guess != magic_number:
        guess = int(input('What is your guess? '))
        count += 1
        if guess > magic_number:
            print('Lower')
        elif guess < magic_number:
            print('Higher')
        else:
            print('You guessed it!')
            
    print(f'It took you {count} guesses. ')
    replay = input('Would you like to play again? (yes/no) ')

