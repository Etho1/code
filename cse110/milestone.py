child = input('What is the price of a child\'s meal?')
adult = input('What is the price of an adult\'s meal?')
child_value = input('How many children are in your party?')
adult_value = input('How many children are in your party?')
tax = input('What is the sales tax rate in your state?')
mozz_stix = input('Would you like to add mozzarella sticks to your meal? ($3.50)')
child = float(child)
adult = float(adult)
child_value = int(child_value)
adult_value = int(adult_value)
tax = float(tax)

child_total = child*child_value
adult_total = adult*adult_value
subtotal = child_total+adult_total
if mozz_stix == 'yes':
    mozz_number = input('How many mozzarella appetizers would you like?')
    mozz_number = float(mozz_number)
    mozz_total = mozz_number*3.50
    subtotal = mozz_total+subtotal
print(f'Subtotal: ${subtotal}.')
tipmepls = input('Would you like to leave a tip?(yes or no)')

tax_total = tax/100
sales_tax = tax_total*subtotal

if tipmepls == 'yes':
    tip_amt = input('what percentage would you like to tip? (10,15,20, or custom)')
    tip_amt = float(tip_amt)
    tip_amt = tip_amt/100
    tip_amt = subtotal*tip_amt
    subtotal = subtotal+tip_amt
print(f'Sales Tax: ${sales_tax:.2f}')

total = sales_tax+subtotal
print(f'Total: ${total:.2f}')

payme = input('What is the payment amount?')
payme = float(payme)
remaining = total-payme
while remaining > 0: #need to keep giving money
    #give us money
    print(f'Your remaining total is: {remaining:.2f}')
    payment = input('What is the payment amount?')
    payment = float(payment)
    remaining = remaining - payment
if remaining < 0:
    remaining = remaining*-1
    print(f'Your change is: {remaining:.2f}') #does not round up, just takes first two decimal places.
print('Have a nice day!')


#check if they paid too much
    # pay the back the change


