numbers = []
num = None
count = -1
print('Enter a list of numbers, type 0 when finished.')
while num != 0:
    num = int(input('Enter number: '))
    count += 1
    if num != 0:
        numbers.append(num)
   
total = 0

for num in numbers:
    total += num
average = total/count
print('The sum is:', total)
print('The average is', average)
print('The largest number is:', max(numbers))
print('The smallest positive value is:', min([num for num in numbers if num > 0]))
numbers.sort()
print('The sorted list is:', numbers)