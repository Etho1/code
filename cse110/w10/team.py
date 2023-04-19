from dataclasses import replace


accounts = []
account_name = None
balances = []
balance = None
highest = .0000000000001
n = None
update = 'yes'
greatest = None
while account_name != 'quit':
    account_name = input('What is the name of this account? ')
    accounts.append(account_name)
    if account_name == 'quit':
        accounts.pop()
    if account_name != 'quit':
        balance = float(input('What is the balance? '))
        balances.append(balance)
    for i in range(len(balances)):
        if highest < balances[i]:
            highest = balances[i]
            n = i

print('\nAccount Information:')
for i in range(len(accounts)):
    print(f'\n{i+1}. {accounts[i].title()} - ${balances[i]}')

total = sum(balances)
average = total/(len(balances))
print(f'\nTotal: ${total:.2f}')
print(f'Average: ${average:.2f}')
print(f'Highest Balance: {accounts[n].title()} - ${highest:.2f}')

while update != 'no':
    update = input('\nDo you want to update an account? ')
    if update != 'no':
        choose = int(input('What account index do you want to update? '))
        replace_val = float(input('What is the new amount? '))
        balances[choose - 1] = replace_val
        print('\nAccount Information:')
        for i in range(len(accounts)):
            print(f'{i+1}. {accounts[i].title()} - ${balances[i]}')

