#!/usr/bin/env python
import socket
print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

##########################################################
# TODO:
# - create a function that takes utilizes arrays as parameters.
# - the function shall add all numbers in the array and then 
# - add 100 to it. use the following elements:
# - [100, 300, 400, 3]

def add100(array):
    sum = 0
    for elements in array:
        sum = sum + elements
    sum = sum + 100
    return sum
print(add100([100, 300, 400, 3]))

##########################################################

# TODO:
# - define a function that takes a string and swaps out
# - all upper case 'O' to upper case 'Ö' and all
# - upper case 'A' to lower case 'ä'
# - replace spaces with dashes
# - use 'On nAra Ostermalm'.

def characterSwap(string):
    x = ''
    for character in string:
        if character == 'O':
            x = x + 'Ö'
        elif character == 'A':
            x = x + 'ä'
        elif character == ' ':
            x = x + '-'
        else:
            x = x + character
    return x
print(characterSwap('On nAra Ostermalm'))
