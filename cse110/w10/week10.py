'''
week10.py
Sis Hansen
'''

# review
nums = []  # empty list we can append to later
nums = [1,5,7,9]  # initialized list
print(f'the third item is: {nums[2]}') # using the index

# get the number of items in the list & print it
size = len(nums)
print(size)
print()
# simple loop through a list to print each item
for num in nums:
    print(num, end=' ')
print()
# loop through a list using the index (and range)
print('\nprint with index')
for i in range(len(nums)): #i will go through values 0... len(nums)
    print(f'{i} - {nums[i]}')
# loop thru list using index and user friendly (+1) display
print("\nuser friendly (don't print 0)")
for i in range(len(nums)): #i will go through values 0... len(nums)
    print(f'#{i + 1} - {nums[i]}')

# use the index for 2 lists 
names = ['bill', 'jenny', 'tom']
ages = [9, 10, 8]
# print('\nloop thru two lists and print both values')
# index + 1 makes it user friendly
for i in range(len(ages)):
    print(f'#{i+1}: {names[i].title()} is {ages[i]} years old')

# replace the second age 
print('\nages before changing 2nd item (index 1):', ages)
ages[1] = 4
print('ages after changing the 2nd item:', ages)
# ask the user which item they want to replace
# if I used user friendly numbers to display, 
# I need to -1 to get the correct index 
replace_index = int(input('what age do you want to replace?:'))
replace_val = int(input('What age should be used?'))
ages[replace_index - 1] = replace_val
# show the list again to show the new age is in the list
print('\naltered list:', ages)



# remove an item from the nums list with pop()
nums = [1,5,7,9]  # initialized list
print('\nbefore popping from nums')
print(nums)
popped_item = nums.pop(2) #default removes the last item in the list

print('\nafter popping from nums', nums)

# print the item removed (popped)
print(popped_item)











# print()

# BONUS: insert a value at index 1 (may confuse some)
# val = (input('Enter a value to insert at index 1: '))
# nums.insert(1, val)
# print('list with value inserted at index 1: ', nums)
# print()

