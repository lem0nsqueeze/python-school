#!/usr/bin/env python3

import socket

print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

# Input: name
name = input("What is your name? ")
print(name)

# Input: age and height
age = int(input("How old are you? "))
height = float(input("How tall are you? "))
print("Your age is:", age, "Your height is:", height)

age = int(input("How old are you? "))
height = float(input("How tall are you? "))
print(f"You are {age} years old and {height} cm tall")

# String input multiplied (string repetition)
number = input("Write a number: ")
print(5 * number)    # e.g. "8" -> "88888"

# Integer input multiplied
number = int(input("Write a number: "))
print(5 * number)    # e.g. 8 -> 40

# Greeting with formatting
name = input("What is your name? ")
print("Hello", name + ",\nWelcome to SATS!")

# Workout cost (integer hours)
rate = 499
hours = int(input("How many hours would you like to work out? "))
print("The cost is", rate * hours, "kr.")

# Workout cost (float hours)
rate = 499
hours = float(input("How many hours would you like to work out? "))
print(f"The rate per hour is: {rate} kr/h\nYour total fee is: %d kr." % (rate * hours))

# Rounding float
print(round(663.671245, 2))  # 663.67

# Customer survey
name = input("Hello,\nPlease enter your first and last name: ")
print("Hello", name + ",\nWelcome to 2226 Group!")
continue_survey = input("This is a customer survey, would you like to continue? ")
print("How nice of you...")

age = int(input("How old are you? "))
print("Interesting...")
print("That means that you will be taking your pension in %d years" % (65 - age))

height = float(input("What is your height (m)? "))
print("Oh wow, are you actually %d cm tall?" % (height * 100))

pulse = input("Do you know your maximum pulse rate? ")
print("Your maximum pulse rate is %d" % (220 - age))

assistance = input("How can I further assist you? ")
print("Ok, please hold... taking a coffee break...")

# Multiply 4 decimal inputs
print("Please input 4 decimal numbers.\nWe will multiply them and get a total value.")
first = float(input("Enter the first value: "))
second = float(input("Enter the second value: "))
third = float(input("Enter the third value: "))
fourth = float(input("Enter the fourth value: "))
result = first * second * third * fourth
print("The total value of the four decimal numbers is: %.2f" % result)

# Loop printing same message
for i in range(5):
    print("This is a loop")

# Loop from 1 to 5
for i in range(1, 6):
    print(i)

# Repeated name outputs
for _ in range(15):
    print("first name")

for _ in range(20):
    print("last name")
