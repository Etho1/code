number = int(input('Please enter a number: '))
quote = 'In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost.'
for i, letter in enumerate(quote):
    if i%number == 0:
        print(f'{letter.upper()}', end='')
    else:
        print(f'{letter}', end='')