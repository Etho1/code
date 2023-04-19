highest = 0
lowest = 1000
highest2 = 0
lowest2 = 1000
highest3 = 0
lowest3 = 1000
lowest_year2 = None
highest_year2 = None
lowest_country = None
lowest_country2 = None
highest_country2 = None
lowest_year = None
highest_country = None
highest_year = None
choice_country2 = []
choice_year = int(input('Enter the year of interest: '))
choice_country = input('Choose a country of interest: ')
with open('life-expectancy.csv') as file:
    next(file)
    for line in file:
        line_list = line.split(',')
        country = line_list[0]
        code = line_list[1]
        year = int(line_list[2])
        expectancy = line_list[3]
        
        if float(expectancy) > float(highest):
            highest = expectancy
            highest_country = country
            highest_year = year
        if float(expectancy) < float(lowest):
            lowest = expectancy
            lowest_country = country
            lowest_year = year
        if country == choice_country.title():
            if float(expectancy) > float(highest3):
                highest3 = expectancy
                highest_year2 = year
            if float(expectancy) < float(lowest3):
                lowest3 = expectancy
                lowest_year2 = year
            choice_country2.append(float(expectancy))
        if year == choice_year:
            if float(expectancy) > float(highest2):
                highest2 = expectancy
                highest_country2 = country
            if float(expectancy) < float(lowest2):
                lowest2 = expectancy
                lowest_country2 = country
    total = sum(choice_country2)
    avg = total/(len(choice_country2))
        # print(f'{country} {code} {year} {expectancy}')

    print(f'\nThe overall max life expectancy is: {highest} from {highest_country} in {highest_year}')
    print(f'The overall min life expectancy is: {lowest} from {lowest_country} in {lowest_year}')
    print(f'\nFor the year {choice_year}:')
    print(f'The overall max life expectancy is: {highest2} from {highest_country2}')
    print(f'The overall min life expectancy is: {lowest2} from {lowest_country2}')
    print(f'\nFor the chosen country {choice_country}')
    print(f'The overall max life expectancy is: {highest3} in the year {highest_year2}')
    print(f'The overall min life expectancy is: {lowest3} in the year {lowest_year2}')
    print(f'The average life expectancy for {choice_country.title()} is {avg}')



