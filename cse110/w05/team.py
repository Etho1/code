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
print(f'Your grade is: {letter}')