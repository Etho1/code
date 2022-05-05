child = input('What is the price of a child\'s meal?')
adult = input('What is the price of an adult\'s meal?')
child_value = input('How many children are in your party?')
adult_value = input('How many children are in your party?')
tax = input('What is the sales tax rate in your state?')
mozz_stix = input('Would you like to add mozzerella sticks to your meal? ($3.50)')
child = float(child)
adult = float(adult)
child_value = int(child_value)
adult_value = int(adult_value)
tax = float(tax)

child_total = child*child_value
adult_total = adult*adult_value
subtotal = child_total+adult_total
if mozz_stix == 'yes':
    subtotal = subtotal+3.50
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
poor = total-payme
rich = payme-total
while payme < total:
    print(f'Your remaining total is: {poor:.2f}')
    payme = input('What is the payment amount?')
    payme = float(payme)
    payme = poor-payme

if payme >= total:
    print(f'Your change is: {rich:.2f}')

