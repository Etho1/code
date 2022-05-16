num1 = input('What is the first number?')
num2 = input('What is the second number?')
num1 = float(num1)
num2 = float(num2)
if num1>num2:
    print('The first number is greater.')
elif num1<num2:
    print('The second number is greater.')
if num1==num2:
    print('The numbers are equal.')
else:
    print('The numbers are not equal.')
animal = 'chicken'
animal2 = input('What is your favorite animal?')
if animal2.lower()==animal:
    print('That\'s my favorite animal too!')
else:
    print('That one is not my favorite.')