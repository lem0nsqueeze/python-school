#!/usr/bin/env python
import socket
print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

##########################################################

# - a function is defined by the programmer
# - def mathAdd_name(arguments)

def math_add_multiply(num1, num2):
    result = num1 * num2 + num1
    return result

print(math_add_multiply(4, 5))
print(math_add_multiply(8, 9))

##########################################################

def math_add_multiply(num1, num2):
    result = num1 * num2 + num1
    return result

y = math_add_multiply(5, 1) + math_add_multiply(3, 1)
print(y)

##########################################################

def mathAdd(num1, num2):
    result = num1 + num2
    return result

x = mathAdd(2, 3)
print(x)

##########################################################

def traingle_area(base, height):
    result = base * height / 2
    return result

area = (traingle_area(5, 7))
print(area)

##########################################################
# TODO:
# - define a function that takes the radius of a circle
# - floato a parameter and then calculates the circle area
# - please user pi

# - use the function to calculate the area of a circle with
# - the radius 3m, a radius with 2m and a radius with 2.5m

import math

def circle_area(radius):
    result = pow(radius, 2) * math.pi
    return result

area1 =(circle_area(3))
area2 =(circle_area(2))
area3 =(circle_area(2.5))

print(area1, area2, area3)

##########################################################
import math

def traingle_area(base, height):
    result = base * height / 2
    return result

input1 = int(input('enter the first number: '))
input2 = int(input('enter the second number: '))

area = (traingle_area(input1, input2))
print(area)

##########################################################

import math

def circle_area(radius1):
    result = pow(radius1, 2) * math.pi
    return result

area1 = float(input('enter the first circle radius: '))
area = (circle_area(area1))
print(area)

def circle_area(radius2):
    result = pow(radius2, 2) * math.pi
    return result

area2 = float(input('enter the second circle radius: '))
area = (circle_area(area2))
print(area)

def circle_area(radius3):
    result = pow(radius3, 2) * math.pi
    return result

area3 = float(input('enter the third circle radius: '))
area = (circle_area(area3))
print(area)

##########################################################
# TODO:
# a) a function that compares two numbers and returns
#    the one with the highest value
# b) use the funtion to get the highest value out of
#    these numbers: 3, 55, -5

def max_number(num1, num2, num3):
    array = [num1, num2, num3]
    return max(array)

print(max_number(3, 55, -5))

##########################################################

def my_function(food):
    for x in food:
        print(x)
    return x
    
fruits = ['apple', 'banana', 'cherry']
my_function(fruits)

##########################################################

def my_function(food):
    for x in food:
        print(x)
    return x
    
fruits = ['apple', 'banana', 'cherry']
my_function(fruits)

##########################################################
# TODO:
# a) compare the words and print the longest word
# b) use the following words in a function:
#    "book" "ruler"   

def warehouse_items(book, ruler):
    office_items = [book, ruler]
    return max(office_items)

print(warehouse_items('book', 'ruler'))

##########################################################
# TODO:
# a) compare the words and print the longest word
# b) use the following words in a function:
#    "book" "ruler"   

def warehouse_items(book, ruler):
    office_items = [book, ruler]
    return max(office_items)

print(warehouse_items('book', 'ruler'))
