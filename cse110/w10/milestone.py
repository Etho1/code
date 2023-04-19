cart = []
prices = []
add = None
price = None
choice = '0'
choice2 = None
total = None
while choice != '5':
    choice = input('\nPlease select one of the following: \n 1. Add item \n 2. View cart \n 3. Remove Item \n 4. Compute total \n 5. Quit \n Please enter an action: ')
    if choice == '1':
        while add != 'quit':
            add = input('What item would you like to add? (Type "quit" when done) ')
            if add != 'quit':
                print(f'\'{add}\' has been added to the cart.')
                cart.append(add)
                price = float(input(f'What is the price of \'{add}\'? '))
                prices.append(price)
    elif choice == '2':
        print()
        for i in range(len(cart)):
            print(f'{i+1}. {cart[i].title()} - ${prices[i]:.2f}')
    elif choice == '3':
        choice2 = int(input('What item would you like to remove? '))
        if choice2 > len(cart):
            print('\nSorry, that is not a valid item number.')
        else:
            choice2 = choice2 - 1
            popped_item = cart.pop(choice2)
            popped_item2 = prices.pop(choice2)
            print(f'\n{popped_item} has been removed.')
    elif choice == '4':
        total = sum(prices)
        print(f'Your total is: {total:.2f}')
if choice == '5':
    print('Thank you. Goodbye.')
        
