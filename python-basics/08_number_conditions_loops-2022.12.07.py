#!/usr/bin/env python3

import socket

print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

##########################################################

def math_add_multiply(num1, num2):
    return num1 * num2 + num1

print(math_add_multiply(4, 5))
print(math_add_multiply(8, 9))

##########################################################

y = math_add_multiply(5, 1) + math_add_multiply(3, 1)
print(y)

##########################################################

def math_add(num1, num2):
    return num1 + num2

x = math_add(2, 3)
print(x)

##########################################################

def triangle_area(base, height):
    return base * height / 2

area = triangle_area(5, 7)
print(area)

##########################################################
# Calculate circle area using radius and pi

import math

def circle_area(radius):
    return math.pi * radius ** 2

print(circle_area(3))
print(circle_area(2))
print(circle_area(2.5))

##########################################################

base = int(input('Enter base of triangle: '))
height = int(input('Enter height of triangle: '))
print(triangle_area(base, height))

##########################################################

radius1 = float(input('Enter first circle radius: '))
print(circle_area(radius1))

radius2 = float(input('Enter second circle radius: '))
print(circle_area(radius2))

radius3 = float(input('Enter third circle radius: '))
print(circle_area(radius3))

##########################################################
# Return max of three numbers

def max_number(num1, num2, num3):
    return max(num1, num2, num3)

print(max_number(3, 55, -5))

##########################################################

def print_items(items):
    for item in items:
        print(item)

fruits = ['apple', 'banana', 'cherry']
print_items(fruits)

##########################################################
# Return the longest word

def longest_word(word1, word2):
    return max(word1, word2, key=len)

print(longest_word('book', 'ruler'))
