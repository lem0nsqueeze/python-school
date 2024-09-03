#!/usr/bin/env python
import socket
print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

##########################################################
# guess a number between 0 - 100

import os

def main():

    initial_value = ''
while True:
    initial_value = int(input('guess a number between 0 - 100: '))

    if initial_value == 20:
        print('Correct!')
        break
    else:
        print('Wrong, try again!')
        continue
        
if __name__ == '__main__':

    main()

##########################################################
# guess a number between 0 - 100

initial_value = ''
while True:
    initial_value = int(input('guess a number between 0 - 100: '))

    if initial_value == 20:
        print('Correct!')
        break
    else:
        print('Wrong, try again!')
        continue

##########################################################
# what does this script do?

i = 0
while i < 5:
    print('this number is:', i)
    i = i + 1
    if i == 3:
        break
print ('The End!')

##########################################################
# write a script that always prints user input
# if input is quit then stop the script

while True:
    initial_value = input("Type something, 'quit' to exit: ")

    if initial_value == 'quit':
        print('thanks for using this script :)')
        break
    else:
        print(initial_value)
        continue

##########################################################
# analyze the code

for initial_value in ('2226-Group'):
    if initial_value == '-':
        break
    print(initial_value)
print('We Are The Future!')

##########################################################
# the scirpt below will print 'i' but skips the number 3

i = 0
while i < 6:
    i = i + 1
    if i == 3:
        continue
    print(i)

##########################################################
# analyze the code

for initial_value in '2226-Group':
    if initial_value == '-':
        continue
    print(initial_value)
print('We Are The Future!')

##########################################################
# An array is a collection of items of the same data
# type stored at contiguous memory locations
# simply put: 
# - a variable is called an array
# - ['index0', 'index1', 'index2'] are called elements
# - each element has an index number starting from 0
# - 'array.append' adds an element to the end of the array
# - 'array.insert' adds an element to a set index in the array 
# - 'array.pop(element index)' removes an element from the array
# - 'array.remove(element name)' removes an element from the array
# - "array'2' = 'index'" replaces element name
# - 'array.clear()' removes all the elements

cars = ['Ford Mustang', 'Dodge Charger', 'Chevy Impala']
print(cars)

cars = ['Ford Mustang', 'Dodge Charger', 'Chevy Impala']
print(cars[0])

cars = ['Ford Mustang', 'Dodge Charger', 'Chevy Impala']
x = cars[0]
print(x)

cars = ['Ford Mustang', 'Dodge Charger', 'Chevy Impala']
x = len(cars)
print(x)

cars = ['Ford Mustang', 'Dodge Charger', 'Chevy Impala']
for x in cars:
    print(x)

cars = ['Ford Mustang', 'Dodge Charger', 'Chevy Impala']
cars.append('Honda Civic')
print(cars)

cars = ['Ford Mustang', 'Dodge Charger', 'Chevy Impala']
cars.insert(1, 'Toyota Supra')
print(cars)

cars = ['Ford Mustang', 'Dodge Charger', 'Chevy Impala']
cars.pop(1)
print(cars)

cars = ['Ford Mustang', 'Dodge Charger', 'Chevy Impala']
cars.remove('Ford Mustang')
print(cars)

cars = ['Ford Mustang', 'Dodge Charger', 'Chevy Impala']
cars[0] = 'Honda Civic'
cars[2] = 'Toyota Supra'
print(cars)

cars = ['Ford Mustang', 'Dodge Charger', 'Chevy Impala']
cars.clear()
print(cars)

##########################################################
# TODO:
# - append element 'Russia' to the end of the array
# - insert element 'Soviet Union' to the array on index '2'
# - pop the element with index '0'
# - clear all elements in the list

array = ['Ukraine', 'NATO', 'EU']
print(array)
array.append('Russia')
print(array)
array.insert(2, 'Soviet Union')
print(array)
array.pop(0)
print(array)
array.clear ()
print(array)

##########################################################
# TODO:
# - write a script to check if 'Apple' is in the list:
# - fruits = ['Orange', 'Apple', 'Banana']

while True:
    fruits = ['Orange', 'Apple', 'Banana']

    if 'Apple' in fruits:
        print('Found Apple!')
        break
    else:
        print('Did not find Apple')
        break

