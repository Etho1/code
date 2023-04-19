'''
week9.py - Lists
Sister Hansen
'''

 
# A list is a COLLECTION!
# Creating a list variable -> good_name = [ ]
# create an empty list to hold ages
ages = []

# create a list of names for bill, tom, sue
names = ['bill', 'tom', 'sue']
# add an age (or several) to the age list and jill to the name list
ages.append(12)
ages.append(10)
ages.append(2)
print(ages)
''' 
remember that for loops are good at going through collections
for item in collection:
    do something each time we get an item (each time the loop iterates)
''' 
# use a for loop to go through the lists and print each item
for age in ages:
    print(age)
print()


# use the debugger to watch the value of name change

''' 
we can access each item in the list through an index
lists are stored in memory in adjacent memory buckets
                         __________________________
     ages -------------> | 10 | 12 | 23 | 34 | 17 | 
                         --------------------------
                            0    1    2    3    4     index   
'''
# print just the second item in the list


# use a for loop to go through the ages list and
# add all the ages together for a total of all ages

total = 0
for age in ages:
    total += age
    print('loop total: ', total)

print('final total: ', total)



'''
#########################################
# day 2
#########################################
import random
# create a list of 15 random numbers (look up list comprehensions)
nums = [random.randint(1,100) for x in range(15)]
print(nums)
print()
 
# find max value in the list (manually)
# need a variable to store the max when I find it
max_val = 0 
# need a loop to go thru the list to check for the max

print('max value is: ', max_val)
print()

# use a built-in function to find max
easy_max = None  # replace None
print('max value is: ', easy_max)
print()

# use a built-in function to find the min and sum
min_num = None
total = None
print(f'the min is {min_num}, the total is {total}')
print()

# create a new list that is sorted
print('original nums list:\n', nums)
sorted_nums = None
print(f'new sorted nums:\n {sorted_nums}')
print()

# sort the list "in-place"
print('original nums list:\n', nums)
pass
print('nums after sorting:\n', nums)
print()

# next week we'll see how to use indexes to 
# go through multiple lists in a for loop at once
'''