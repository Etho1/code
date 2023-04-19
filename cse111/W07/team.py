import random


def main():
    numbers = [16.2,75.1,52.3]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)


def append_random_numbers(numbers_list,quantity = 1):
    for int in range(quantity):
        random_int = random.uniform(0,100)
        random_float = round(random_int,1)
        numbers_list.append(random_float)
main()


