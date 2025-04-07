#!/usr/bin/env python3

import socket

print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

# Arithmetic operations
print(4 + 2)             # 6
print(4 - 2)             # 2
print(4 * 2)             # 8
print(6 / 2)             # 3.0
print(38 + 11 + 8)       # 57

# Demonstrating string vs. evaluated expression
print("38 + 11 + 8")     # 38 + 11 + 8
print("you'll have to pay:")
print(38 + 11 + 8)       # 57

# Concatenated and formatted output
print("you'll have to pay:", 38 + 11 + 8, "kr.")              # you'll have to pay: 57 kr.
print("you'll have to pay:\n", 38 + 11 + 8, "kr.")            # newline with indent
print(f"you'll have to pay:\n{38 + 11 + 8} kr.")              # f-string
print("you'll have to pay:\n%d kr." % (38 + 11 + 8))          # printf-style

# Escape sequences and tabs
print("Languages:\nPython\tJava\nJavaScript")

# More expressions
print(12 - 7)                                # 5
print(24 / 3 + 9)                            # 17.0
print(8 * 2 * (5 - 3) + 16 / 4 - 1)          # 35.0

# Newlines and basic string manipulation
print("Hello!\nHow are you?")               # Hello! \n How are you?

print("1" + "1")                             # 11
print(3 * "1")                               # 111
print(1 + 1)                                 # 2
print(1 * 3)                                 # 3

print("hello", "hello")                      # hello hello
print("hello\t" * 10)                        # repeated with tabs

# Speed × time example
speed = 70
time = 1.5
distance = speed * time

print("If you drive at a speed of 70 km/h in 1.5 hours, then you can make a")
print(distance)
print("km. trip")

print(f"If you drive at a speed of {speed} km/h in {time} hours, then you can make a {distance} km. trip")
