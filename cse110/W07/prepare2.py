candy = input('May I have a piece of candy? ')
while candy.lower() != 'yes':
    candy = input('May I have a piece of candy? ')

if candy.lower() == 'yes':
    print('Thank you.')