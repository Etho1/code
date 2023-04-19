import csv

def read_dictionary(filename):
    """
    Reads a CSV file and returns a dictionary where the keys are the first
    column and the values are the remaining columns.
    """
    dictionary = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header row
        for row in reader:
            key = row[0]
            value = row[1:]
            dictionary[key] = value
    return dictionary

def main():
    # Read the products.csv file and create a dictionary of products
    products = read_dictionary('products.csv')

    # Read the request.csv file and create a dictionary of items ordered by the customer
    request = read_dictionary('request.csv')

    # Calculate the total price of the order
    total_price = 0
    for item, quantity in request.items():
        if item in products:
            price = float(products[item][0])
            total_price += price * int(quantity)

    # Print the receipt
    print("********** RECEIPT **********")
    for item, quantity in request.items():
        if item in products:
            name = products[item][1]
            price = float(products[item][0])
            subtotal = price * int(quantity)
            print(f"{name} x {quantity}: ${subtotal:.2f}")
    print(f"Total: ${total_price:.2f}")
    print("*****************************")

if __name__ == '__main__':
    main()
