import csv

# Read the CSV file into a dictionary
students_dict = {}
with open('students.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the first line
    for row in csv_reader:
        i_number, name = row
        students_dict[i_number] = name

# Get the I-Number from the user
i_number = input("Enter an I-Number: ")

# Print the corresponding student name or "No such student"
if i_number in students_dict:
    print(students_dict[i_number])
else:
    print("No such student")
