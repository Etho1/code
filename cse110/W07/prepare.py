num = int(input('Please type a positive number: '))
while num < 0:
    print('Sorry, that is a negative number. Please try again.')
    num = int(input('Please type a positive number: '))
    
if num > 0:
    print(f'The number is: {num}')
