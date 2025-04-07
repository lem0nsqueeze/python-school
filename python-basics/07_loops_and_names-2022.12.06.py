#!/usr/bin/env python3

import socket

print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

##########################################################

# Prints all fruits and breaks after first iteration
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
    if fruit == 'banana':
        print()
    break

##########################################################

# Combines adjectives with fruits
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']
for x in adj:
    for y in fruits:
        print(x, y)

##########################################################

# Check if 1 is in the list
numbers = [1, 2, 3, 4]
if 1 in numbers:
    print('found')
else:
    print('not found')

##########################################################

# Remove 'user1' if present
users = ['user1', 'user2', 'user3', 'user4', 'user5']
if 'user1' in users:
    users.remove('user1')
    print(users)

##########################################################

# Print all users except 'user3'
usernames = ['user1', 'user2', 'user3', 'user4', 'user5']
for name in usernames:
    if name == 'user3':
        continue
    print(name)

##########################################################

# Array slicing examples
array = [1, 4, 9, 16, 25, 90]
print(array[3:])    # 16, 25, 90
print(array[:3])    # 1, 4, 9
print(array[2:4])   # 9, 16

##########################################################

# String slicing
country = 'Sverige'
print(country[:2])     # Sv
print(country[3:6])    # rig
print(country[5:])     # ge

##########################################################

# Min, max, sum, and power
numbers = [1, 2, 3, 4, 5]
print(min(numbers))           # 1
print(max(numbers))           # 5

numbers = [1, 2, 3, 4, 5, 6]
print(sum(numbers))           # 21

x = pow(2, 4)
print(x)                      # 16

##########################################################

# Copying list
numbers = [1, 2, 3, 4, 5, 6]
jensen = numbers[:]
print(numbers)
print(jensen)

##########################################################

# TODO: Perform array operations
num = [1, 5, -29, 86, 7, -8]
Stockholm = num[:]
print(min(num))         # -29
print(max(num))         # 86
print(sum(num))         # 62
print(Stockholm)

##########################################################

# Math operations
import math

x = math.sqrt(64)
y = int(math.sqrt(64))
z = float(math.sqrt(64))
print(x, y, z)

x = math.pi
print('The value of pi is', x)
print('The value of pi is approximately %f' % x)
print('The value of pi is approximately %5.3f' % x)

r = 4
area = pow(r, 2) * math.pi
print('The area of the circle is', area, 'cm^2')

##########################################################

# TODO: Number logic with math
user_input = float(input('Please input a number: '))

while True:
    if user_input > 20:
        print(math.sqrt(user_input))
    else:
        print(math.pow(user_input, 2))
    break
