youngest = 1000
youngest_name = None
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
for line in people:
    clean_line = line.strip()
    line_list = clean_line.split()
    name = line_list[0]
    age = int(line_list[1])
    print(f'Name: {name} Age: {age}')
    if age < youngest:
        youngest = age
        youngest_name = name
print(f'The youngest is {youngest_name}, who is {youngest} years old.')
