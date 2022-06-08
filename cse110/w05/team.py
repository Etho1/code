grade = input('What is your grade percentage?')
grade = float(grade)
if grade>= 90:
    letter = 'A'
elif grade>= 80:
    letter = 'B'
elif grade>= 70:
    letter = 'C'
elif grade>= 60:
    letter = 'D'
else:
    letter = 'F'
sign1 = grade%10
if sign1 >=7:
    sign2='+'
elif sign1 <3:
    sign2='-'
else:
    sign2=''
if grade > 93:
    sign2=''
if grade <59:
    sign2=''
print(f'Your grade is: {letter}{sign2}')