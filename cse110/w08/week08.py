# 1) loop to print 1 through 5 (using a range)


# 2) loop to print "Hello World" a user specified number of times
print()


# 3) loop to print each letter in a string (three ways)
print()
my_string = "Have a nice day."
for letter in my_string:
    print(letter)
print()
for index in range(len(my_string)): #collection: 0,1,2,3,... len(my_string)-1
    print(my_string [index])
print()
for i, letter in enumerate(my_string):
    print(f'{i=} - {letter}')
# 4) loop to print each item in a list
print()
my_list = [1,3,5,7,9]


# team activity - looping through strings 