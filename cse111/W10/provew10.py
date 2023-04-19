# ETHAN SPENCER CSE111 


import csv
from datetime import datetime

def read_stock(filename):
    """
    Reads a CSV file and returns a dictionary where the keys are the first
    column and the values are the remaining columns.
    """
    dictionary = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header row
        for row in reader:
            es_key = row[0]
            value = [row[1], row[2]]
            dictionary[es_key] = value
    return dictionary

def read_order(filename):
    """
    Reads a CSV file and returns a dictionary where the keys are the first
    column and the values are the remaining columns.
    """
    dictionary = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header row
        for row in reader:
            es_key = row[0]
            es_qty = int(row[1])
            if es_key in dictionary:
                dictionary[es_key] = int(dictionary[es_key]) + int(es_qty)
            else:
                dictionary[es_key] = es_qty
    return dictionary

def print_receipt(store_name, request, products):
    """
    Prints a receipt for a customer's grocery order.
    """
    try:
        # Calculate the total price of the order
        es_total_price = 0
        for item, quantity in request.items():
            if item in products:
                es_price = float(products[item][1])
                es_total_price += es_price * float(quantity)

        # Print the receipt
        print(f"\n{store_name.upper()}\n")
        print("********** RECEIPT **********")
        for item, quantity in request.items():
                es_name = products[item][0]
                es_price = float(products[item][1])
                es_subtotal = es_price
                print(f"{es_name}: {quantity} @ ${es_subtotal:.2f}")
        print(f"\nNumber of items: {sum(request.values())}")
        print(f"Subtotal: ${es_total_price:.2f}")
        es_sales_tax = es_total_price * 0.06
        print(f"Sales tax: ${es_sales_tax:.2f}")
        es_total_due = es_total_price + es_sales_tax
        print(f"Total due: ${es_total_due:.2f}")
        print("\nTHANK YOU FOR SHOPPING WITH US!")
        now = datetime.now()
        print(f"Date and time of purchase: {now.strftime('%m/%d/%Y %I:%M %p')}")
    except FileNotFoundError:
        print("Error: missing file")
    except PermissionError:
        print("Error: Permission denied.")
    except KeyError:
        print(f"Error: unknown product ID in the request.csv file \"{item}\"")

def main():
    # Read the products.csv file and create a dictionary of products
    try:
        es_products = read_stock('products.csv')
    except FileNotFoundError:
        print("Error: File not found.")
        return
    except PermissionError:
        print("Error: Permission denied.")
        return

    # Read the request.csv file and create a dictionary of items ordered by the customer
    try:
        es_request = read_order('request.csv')
    except FileNotFoundError:
        print("Error: File not found.")
        return
    except PermissionError:
        print("Error: Permission denied.")
    
        return

    # Print the receipt
    print_receipt("Etho's market", es_request, es_products)

if __name__ == '__main__':
    main()