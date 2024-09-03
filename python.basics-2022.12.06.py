#!/usr/bin/env python
import socket
print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

##########################################################

# prints apple and breaks on banana
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
    if fruits == 'banana':
        print()
    break

##########################################################

# adds the two arrays together and prints
# according to index number 
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']
for x in adj:
    for y in fruits:
        print(x,y)

##########################################################

# the following code prints 'found' if number 1 is in the list
numbers = [1,2,3,4]
if 1 in numbers:
    print('found')
else:
    print('not found')

##########################################################

# prints all users but removes 'user1'
users = ['user1', 'user2', 'user3', 'user4', 'user5']
if 'user1' in users:
    users.remove('user1')
    print(users)

##########################################################

# prints all users but 'user3'
usernames = ['user1', 'user2', 'user3', 'user4', 'user5']
for x in usernames:
    if x == 'user3':
        continue
    print(x)

##########################################################

# prints 16, 25, 90 and skips the previous
array = [1, 4, 9, 16, 25, 90]
print(array[3:])

# prints 1, 4, 9 and skips the rest
array = [1, 4, 9, 16, 25, 90]
print(array[:3])

# prints 9 and 16 but not the rest
array = [1, 4, 9, 16, 25, 90]
print(array[2:4])

##########################################################

# splits 'Sverige' into 'Sv' 'rig' 'ge'
country = 'Sverige'
print(country[:2])
print(country[3:6])
print(country[5:])

##########################################################

# prints min and max number
numbers = [1, 2, 3, 4, 5]
print(min(numbers))
print(max(numbers))

# prints sum of numbers
numbers = [1, 2, 3, 4, 5,6]
print(sum(numbers))

# prints 2*2*2*2
x = pow(2, 4)
print(x)

##########################################################

# prints numbers for 'numbers' and for 'jensen'
numbers = [1, 2, 3, 4, 5,6]
jensen = numbers[:]
print(numbers)
print(jensen)

##########################################################
# TODO:
# 1. print the lowest number in array
# 2. print the highest number in array
# 3. sum all the elements in the array
# 4. copy the array and save in variable 'Stockholm'

num = [1, 5, -29, 86, 7, -8]
Stockholm = num[:]
print(min(num))
print(max(num))
print(sum(num))
print(Stockholm)

##########################################################

# imports the math module and prints the square root
import math

x = math.sqrt(64)
y = int(math.sqrt(64))
z = float(math.sqrt(64))
print(x,y,z)

# prints the value of pi
import math
x = math.pi
print('the value of pi is', (x))
print('The value of pi is approximately %f'%(x))
print('The value of pi is approximately %5.3f' % (x))

# r = radius of circle. prints the square centimeters of the circle
import math
r = 4
area = pow(r, 2) * math.pi
print('the area of the circle is',(area), 'cm^2')

##########################################################
# TODO:
# - write a script that asks the user to input a number.
# - if the number is more than 20 then print the square root
# - of that number.
# - if not then print the number^2. use a loop

import math

userInput = float(input('please input a number: '))

while True:
    if userInput > 20:
        print(math.sqrt(userInput))
    else:
        print(math.pow(userInput, 2))
    break
