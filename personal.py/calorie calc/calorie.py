def calorie(mf,weight, height, age):
    '''calculates calorie expendature'''
    if mf.lower() == 'm':
        calorie_expendature = 66.5 + (13.75 * weight) + (5.003 * height) - (6.75 * age)
    elif mf.lower() == 'f':
        calorie_expendature = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
    return calorie_expendature
def kilogram(lbs):
    '''converts lbs to kg'''
    kg = (lbs) * 2.205
    return kg
def centimeter(feet):
    '''converts feet to centimeters'''
    cm = (feet) * 30.48

# Ask user for their home country
location = input('What country do you live in? ')

# Ask user if male of female
mf = input('What is your biological sex? (M or F) ')
# Ask user for age
age = float(input('What is your age? '))
if location == 'USA':
    # Ask user for height
    feet = float(input('What is your height in feet? '))
    # Ask user for weight
    lbs = float(input('What is your weight in lbs? '))
    # Convert lbs to kg
    weight = kilogram(lbs)
    # Convert cm to feet
    height = centimeter(feet)
else: 
    height = float(input('What is your height in cm? '))
    # Ask user for weight
    weight = float(input('What is your weight in kg? '))

# Determine calorie expendature
calorie_expendature = calorie(mf,weight,height,age)
print(f'Your daily calorie expandature, not including extra exercise is: {calorie_expendature}')