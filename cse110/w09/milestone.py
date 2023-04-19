cart = []
add = None
choice = '0'
while choice != '5':
    choice = input('Please select one of the following: \n 1. Add item \n 2. View cart \n 3. Remove Item \n 4. Compute total \n 5. Quit \n Please enter an action: ')
    if choice == '1':
        add = input('What item would you like to add? ')
        print(f'\'{add}\' has been added to the cart.')
        cart.append(add)
    
    if choice == '2':
        for i in (cart):
            print(i)
