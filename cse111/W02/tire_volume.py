#Ethan Spencer CSE111

import math
def get_width():
    width = int(input('Enter the Width of the tire in mm (ex 205): '))
    return width
def get_ratio():
    ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
    return ratio
def get_dia():
    diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))
    return diameter
def calc_volume(esw,esa,esd):
    volume = (math.pi*(esw**2)*esa*(esw*esa + (2540 * esd))) / 10000000000
    return volume
def tire_finder(esw,esa,esd):
    if esw == 205 and esa == 60 and esd == 15:
        print('A set of tires fitting your needs would be the Stratus AS, priced at $91.99 per tire')
        es_add_to_cart = input('Would you like to purchase these tires?Y/N')
    elif esw == 185 and esa == 60 and esd == 16:
        print('A set of tires fitting your needs would be the Snowtrac 5, priced at $181.99 per tire')
        es_add_to_cart = input('Would you like to purchase these tires?Y/N')
    elif esw == 385 and esa == 70 and esd == 16:
        print('A set of tires fitting your needs would be the Open Country M/T, priced at $602.00 per tire')
        es_add_to_cart = input('Would you like to purchase these tires?Y/N')
    elif esw == 35 and esa == 13.5 and esd == 20:
        print('A set of tires fitting your needs would be the Open Country R/T, priced at $603.00 per tire')
        es_add_to_cart = input('Would you like to purchase these tires? Y/N')
    else:
        print('Unfortunately we could not find any tires of the specific size.')
        es_add_to_cart = 'n'
    return es_add_to_cart
def main():
    esw = get_width()
    esa = get_ratio()
    esd = get_dia()
    esv = calc_volume(esw,esa,esd)
    print(f'The approximate volume is {esv:.2f} liters')
    esbuy = tire_finder(esw,esa,esd)

    if esbuy.lower() == 'y':
        esnum = input('Please enter your phone number: (XXX)-XXX-XXXX')
    
    #import date & time
    from datetime import datetime
    #determine date & time
    escurrent_dt = datetime.now(tz=None)
    # print(f'{escurrent_dt:%Y-%m-%d}')
    if esbuy.lower() == 'y':
        with open('volumes.txt','at') as volumes_file:
        #append info to txt file
            print(f'{escurrent_dt:%Y-%m-%d}, {esw}, {esa}, {esd}, {esv:.2f}, {esnum}', sep=' ', end='\n', file=volumes_file, flush=False)
    else:
    #Open file named volumes.txt
        with open('volumes.txt','at') as volumes_file:
            #append info to txt file
            print(f'{escurrent_dt:%Y-%m-%d}, {esw}, {esa}, {esd}, {esv:.2f}', sep=' ', end='\n', file=volumes_file, flush=False)
call = main()