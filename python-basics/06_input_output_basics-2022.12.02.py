#!/usr/bin/env python3

import socket

print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

##########################################################
# Guess a number between 0 - 100

import os

def main():
    while True:
        guess = int(input("Guess a number between 0 - 100: "))
        if guess == 20:
            print("Correct!")
            break
        else:
            print("Wrong, try again!")

if __name__ == '__main__':
    main()

##########################################################
# Same guess logic without function

while True:
    guess = int(input("Guess a number between 0 - 100: "))
    if guess == 20:
        print("Correct!")
        break
    else:
        print("Wrong, try again!")

##########################################################
# Loop with break condition

i = 0
while i < 5:
    print("This number is:", i)
    i += 1
    if i == 3:
        break
print("The End!")

##########################################################
# Print input until 'quit' is entered

while True:
    value = input("Type something, 'quit' to exit: ")
    if value == 'quit':
        print("Thanks for using this script :)")
        break
    else:
        print(value)

##########################################################
# Analyze character loop with break

for char in "2226-Group":
    if char == '-':
        break
    print(char)
print("We Are The Future!")

##########################################################
# Loop skips number 3

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

##########################################################
# Analyze character loop with continue

for char in "2226-Group":
    if char == '-':
        continue
    print(char)
print("We Are The Future!")

##########################################################
# Array operations demo

cars = ['Ford Mustang', 'Dodge Charger', 'Chevy Impala']
print(cars)

print(cars[0])

x = cars[0]
print(x)

length = len(cars)
print(length)

for car in cars:
    print(car)

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

cars.clear()
print(cars)

##########################################################
# TODO: perform operations on 'array'

array = ['Ukraine', 'NATO', 'EU']
print(array)

array.append('Russia')
print(array)

array.insert(2, 'Soviet Union')
print(array)

array.pop(0)
print(array)

array.clear()
print(array)

##########################################################
# TODO: check if 'Apple' is in the list

fruits = ['Orange', 'Apple', 'Banana']
if 'Apple' in fruits:
    print('Found Apple!')
else:
    print('Did not find Apple')
