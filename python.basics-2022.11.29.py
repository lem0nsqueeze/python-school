#!/usr/bin/env python3

import socket

print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

# Print numbers from 1 to 16 with step of 3
for n in range(1, 17, 3):
    print(n)

# Print "jensen!" four times
for _ in range(4):
    print("jensen!")

# Infinite loop with nested ranges
while True:
    for x in range(1, 12):
        for y in range(1, 101):
            for z in range(-100, 6):
                print(x, y, z)
                continue

# Even numbers from 0 to 100
for n in range(0, 102, 2):
    print(n)

# First 51 even numbers
for n in range(0, 51):
    print(2 * n)

# Multiplication table for 1
number = 1
for n in range(1, 11):
    print(number, 'x', n, '=', number * n)

# Full multiplication tables from 1 to 10
for x in range(1, 11):
    print(f"\n\nTable {x}\n")
    for y in range(1, 11):
        print(f"{x} x {y} = {x * y}")

# Positive number check
num = 3
if num > 0:
    print(num, "is a positive number.")
    print("This is always printed.")

# ---------------------------------------------------------
# Save the following scripts in separate files to run
# ---------------------------------------------------------

# patient.py
#!/usr/bin/env python3

import os

def main():
    while True:
        response = input("Are you an adult? y/n: ").lower()
        if response == 'y':
            print("Your recommended intake is 750 mg/day")
            break
        elif response == 'n':
            print("Your recommended intake is 500 mg/day")
            break
        else:
            print("Please answer with 'y' or 'n'")

if __name__ == '__main__':
    main()

# weight_based_dosage.py
#!/usr/bin/env python3

import os

def main():
    while True:
        try:
            weight = float(input("What is your weight (kg)? "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if weight < 20:
            print("Your recommended intake is 500 mg/day")
        elif 20 <= weight <= 40:
            print("Your recommended intake is 750 mg/day")
        else:
            print("Your recommended intake is 1000 mg/day")
        break

if __name__ == '__main__':
    main()