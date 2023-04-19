# Ethan Spencer
def esgetsubtotal():
    essubtotal = float(input('Please enter the subtotal: '))
    return essubtotal
esst = .06 

    
#import date & time
from datetime import datetime
#determine date & time
escurrent_dt = datetime.now()
esdow = escurrent_dt.weekday()
print(f'Day Of Week: {esdow}')
#ask for subtotal

#determine if discount is earned
def displaydiscountamt(subtotal):
    esdiscountamt = 0
    if esdow == 2 or esdow == 3:
        if subtotal > 50:
            esdiscountamt = .1
        # else:
            esdicountamt = 0
    else:
         esdiscountamt = 0
    esdiscountamtfinal = subtotal * esdiscountamt
    if esdiscountamtfinal > 0:
        print(f'Discount amount: {esdiscountamtfinal:.2f}')
        # esdiscountamtfinal = float(esdiscountamtfinal)
    return esdiscountamtfinal
#add discount

#display sales tax, total, and discount if earned
def displaysalestax(esst, subtotal, esdiscountamtfinal):
    estaxamt = esst * (subtotal + esdiscountamtfinal)
    print (f'Sales tax amount: {estaxamt:.2f}')
    return estaxamt
def displaytotal(subtotal, esdiscountamtfinal, estaxamt):
    estotal = (subtotal - esdiscountamtfinal) + estaxamt
    print(f'Total: {estotal:.2f}')
    return estotal

def main():
    subtotal = esgetsubtotal()
    esdiscountamt = displaydiscountamt(subtotal)
    essalestax = displaysalestax(esst, subtotal, esdiscountamt)
    total = displaytotal(subtotal, esdiscountamt, essalestax)
    return total

call = main()

