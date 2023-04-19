es_age = int(input('Please enter your age: '))
es_hr_max = 220 - es_age
es_hr_recmax = es_hr_max * .85 
es_hr_min = es_hr_max * .65
print(f'When you exercise to strengthen your heart, you should keep your heart rate between {es_hr_min:.0f} and {es_hr_recmax:.0f} beats per minute.')