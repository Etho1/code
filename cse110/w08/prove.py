import os
secret_word = input('Have a friend enter a 5 letter secret word for you to guess: ')
os.system('cls')
guess = ''
count = 0
while guess.lower() != secret_word.lower():
    guess = input('\nWhat is your guess? ')
    count += 1
    if guess.lower() != secret_word.lower():
        print('Your hint is: ', end='')
        for i, letter in enumerate(guess):
            if guess[i] == secret_word[i].lower():
                print(guess[i].upper(), end='')
            elif guess[i] in secret_word.lower():
                print(guess[i].lower(), end='')
            else:
                print('_ ', end='')
if guess.lower() == secret_word.lower():
    print('\nCongratulations! You guessed it!')
    print(f'It took you {count} guesses.')
print()