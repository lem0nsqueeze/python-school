#!/usr/bin/env python3

import socket

print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

import os

def main():
    while True:
        try:
            weight = float(input("What is your weight? "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if weight < 20:
            print("Your recommended intake is 500 mg/day")
        elif 20 <= weight <= 40:
            print("Your recommended intake is 750 mg/day")
        elif 41 <= weight <= 60:
            print("Your recommended intake is 1000 mg/day")
        else:
            print("Your recommended intake is 1000 mg/day")
        break

if __name__ == '__main__':
    main()