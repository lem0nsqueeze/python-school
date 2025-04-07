#!/usr/bin/env python3

import socket

print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

##########################################################

response = ''

while True:
    response = input('Are you over 18 years old? y/n: ')
    if response.lower() == 'y':
        print('Good for you!')
        continue
    elif response.lower() == 'n':
        print('You are not old enough to use this program')
        break
    else:
        print('\nType y or n\n')
        continue

##########################################################

# Check if number is more than, equal to, or less than 40
value = float(input('Enter a number: '))
if value > 40:
    print('The number is more than 40!')
elif value == 40:
    print('The number is equal to 40!')
else:
    print('The number is less than 40!')

##########################################################

n = 0
while n < 10:
    print(n)
    n += 2

n = 1
while True:
    print(n)
    n += 2

n = 1
while n < 15:
    print(n)
    n += 2

n = 0
while n < 200:
    print(n)
    n += 2

n = 100
while n > 0:
    print(n)
    n -= 1

counter = 0
while counter < 3:
    print('Inside loop')
    counter += 1
print('Outside while')

##########################################################

count = 0
while count < 5:
    print(count, 'is less than 5')
    count += 1
print(count, 'is not less than 5')

##########################################################

# Print even numbers:
# a) less than or equal to 200
n = 0
while n <= 200:
    print(n)
    n += 2

# b) from 20 to 40
n = 20
while n <= 40:
    print(n)
    n += 2

# c) infinite loop (intended to keep printing even numbers)
n = 0
while True:
    print(n)
    n += 2

##########################################################

# Evaluate expressions
for y in range(1, 11):
    if 2 * y + 4 == 14:
        print('y =', y, 'is the result')

for y in range(1, 11):
    if 4 * y - 2 == 38:
        print('y =', y, 'is the result')

##########################################################

# Sum of numbers from 1 to n
n = float(input('Please input a number: '))
total = 0
i = 1

while i <= n:
    total += i
    i += 1
print('The sum is:', total)

# Infinite loop version
while True:
    n = float(input('Please input a number: '))
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    print('The sum is:', total)

##########################################################

# Example of using Python built-in sum
marks = [65, 71, 68, 74, 61]
total_marks = sum(marks)
print(total_marks)  # Output: 339

##########################################################