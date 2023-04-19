quote = input('Enter a text: ')
# quote = 'In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost.'
replay = 'yes'
while replay == 'yes':
    number = int(input('Please enter a number: '))
    for i, letter in enumerate(quote):
        if i%number == 0:
            print(f'{letter.upper()}', end='')
        else:
            print(f'{letter}', end='')
        
    replay = input('\nWould you like to enter a new number? (yes/no) ')
if replay == 'no':
    print('Thank you for playing.')