# Write a function to calculate wind chill based on temp and speed
def calc_windspeed(temp, speed):
    '''Computes wind speed'''
    wind_chill = 35.74 + 0.6215*temp - 35.75 * speed**0.16 + 0.4275*temp*speed**0.16
    return wind_chill
# Write a function to convert C to F
def temp_convert(temp):
    '''Converts from celsius to fahrenheit'''
    fahrenheit = (temp) * 9/5 + 32
    return fahrenheit
# Ask user for temp
temp = float(input('What is the temperature? '))

# Ask if in C or F
unit = input('Is the temperature in C or F? ')

#if they use C, convert to F
    #Call convert function
if unit.lower() == 'c':
    temp = temp_convert(temp)

#Write a loop to go thru wind speeds 5 to 60mph, by 5's
for velocity in range(5,61,5):
    # Calc and display wind chill for each speed (2 decimals)
    windchill = calc_windspeed(temp, velocity)
    print(f'At temperature {temp}F, and wind speed {velocity}, the windchill is: {windchill:.2f}F')