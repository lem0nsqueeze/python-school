#!/usr/bin/env python
import socket
print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

##########################################################

initial_value = ''

while True:
    initial_value = input('Are you over 18 years old? y/n: ')

    if initial_value.lower() == 'y':
        print('Good for you!')
        continue
    elif initial_value.lower() == 'n':
        print('You are not old enough to use this program')
        break
    else:
        print('\ntype y or n\n')
        continue

##########################################################

# Write a script that tells if the input number is:
# more than 40.
# equal to 40.
# less than 40.

initial_value = float(input('Enter a number: '))
if initial_value > 40:
    print('the number is more than 40!')
elif initial_value == 40:
    print('the number is equal to 40!')
elif initial_value < 40:
    print('the number is less than 40!')

##########################################################

n = 0

while n < 10:
    print(n)
    n = n + 2

#
n = 1

while True:
    print(n)
    n = n + 2

#
n = 1

while n < 15:
    print(n)
    n = n + 2

#
n = 0

while n < 200:
    print(n)
    n = n + 2

#
n = 100
while n > 0:
    print(n)
    n = n - 1

#
counter = 0

while counter < 3:
    print('Inside loop')
    counter = counter + 1
print('Outside while')

##########################################################

count = 0
while count < 5:
    print(count, 'is less than 5')
    count = count + 1
print(count, 'is not less than 5')

##########################################################

# write a script that outputs positive even numbers:
# a) less or equal to 200
# b) more or equal to 20 but less or equal to 40
# c) without break

# a)
n = 0

while n <= 200:
    print(n)
    n = n + 2

# b)
n = 20

while n <= 40:
    print(n)
    n = n + 2

# c)
n = 0

while True:
    0 <= 200
    print(n)
    n = n + 2

##########################################################

# what does the script below do?
for y in range(1, 11):
    if 2 * y + 4 == 14:
        print('y =',y,'is the result')

#
for y in range(1, 11):
    if 4 * y -2 == 38:
        print('y =',y,'is the result')

##########################################################

# write a script that outputs any input number and prints
# the following:
# 1 + 2 + 3 + ... + n

#
n = float(input('please input a number: '))
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1
print('The sum is: ', sum)

# infinite loop
while True:
    n = float(input('please input a number: '))
    sum = 0
    i = 1

    while i <= n:
        sum = sum + i
        i = i + 1
    print('The sum is: ', sum)

##########################################################

# do not use 'sum' since it's booked by python
# example:

marks = [65, 71, 68, 74, 61]

# find sum of all marks
total_marks = sum(marks)
print(total_marks)

# Output: 339

##########################################################

