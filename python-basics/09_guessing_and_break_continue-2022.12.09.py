#!/usr/bin/env python3

import socket

print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

##########################################################
# Add all numbers in array and add 100

def add_100(numbers):
    return sum(numbers) + 100

print(add_100([100, 300, 400, 3]))

##########################################################
# Replace specific characters in string

def character_swap(text):
    result = ''
    for char in text:
        if char == 'O':
            result += 'Ö'
        elif char == 'A':
            result += 'ä'
        elif char == ' ':
            result += '-'
        else:
            result += char
    return result

print(character_swap('On nAra Ostermalm'))
