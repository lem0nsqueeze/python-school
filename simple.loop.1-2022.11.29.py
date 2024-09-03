#!/usr/bin/env python
import socket
print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

import os

# main function
def main():

    # loop
    weight = ''
while True:
    weight = float (input('what is your weight? '))

    if weight < 20:
        print('Your recommended intake is 500 mg/day')
        break
    elif 20 <= weight <= 40:
        print('Your recommended intake is 750mg/day')
        break
    elif 41 <= weight <= 60:
        print('Your recommended intake is 1000mg/day')
        break
    else:
        print('Your recommended intake is 1000mg/day')
        break
        
if __name__ == '__main__':
    # invokes main function
    main()
