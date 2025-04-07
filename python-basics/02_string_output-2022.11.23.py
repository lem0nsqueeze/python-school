#!/usr/bin/env python3

import socket

# Intro message, exits immediately after
print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

# Basic math operations
print(7**2)             # Exponentiation: 7^2 = 49
print(7//2)             # Integer division: 7 // 2 = 3
print(49**0.5)          # Square root of 49 = 7.0
print(2**6)             # 2 raised to power 6 = 64

# Division comparisons
print(9/2, "and", 9//2)             # Float and integer division: 4.5 and 4
print(11/6, "and", 11//6)           # 1.83... and 1
print(21/8, "and", 21//8)           # 2.625 and 2

# Rectangle: width = 3, length = 4
print("A rectangle has the width of 3 cm and the length of 4 cm.")
print("The circumference is", (3 + 4) * 2, "centimeters.")     # (3+4)*2 = 14
print("The area is", 3 * 4, "squarecentimeters.")              # 3*4 = 12

# Same with line breaks and formatting
print("A rectangle has the width of 3 cm and the length of 4 cm.\n"
      "The circumference is:", (3 + 4) * 2, "centimeters\n"
      "The area is:", 3 * 4, "squarecentimeters")

# Multiplication with variables
x = 10
y = 15
print(x * y)            # 10*15 = 150

# Rectangle with width = 3, length = 4
x = 3
y = 4
print("A rectangle has the width of 3 cm and the length of 4 cm.\n"
      "The circumference is:", (x + y) * 2, "centimeters\n"
      "The area is:", x * y, "squarecentimeters")

# Static error message
error = "CRITICAL ERROR, PLEASE TRY AGAIN!"
print(error)

# Expression with variables
a = 5
b = 10
c = (2 * a) - (3 * b)   # (2*5)-(3*10) = 10 - 30 = -20
print(c)

# Rectangle with width = 5, length = 8
x, y = 5, 8
print("A rectangle has the width of 5 cm and the length of 8 cm.\n"
      "The circumference is:", (x + y) * 2, "centimeters\n"
      "The area is:", x * y, "squarecentimeters")

# Rectangle with width = 92, length = 230
x, y = 92, 230
print("A rectangle has the width of 92 cm and the length of 230 cm.\n"
      "The circumference is:", (x + y) * 2, "centimeters\n"
      "The area is:", x * y, "squarecentimeters")

# Rectangle in meters
x, y = 1, 3
print("A rectangle has the width of 1 m and the length of 3 m.\n"
      "The circumference is:", (x + y) * 2, "meter\n"
      "The area is:", x * y, "squaremeters")

# Simple multiplication
x, y = 2, 3
print(x * y)            # 2*3 = 6

# Shopping cart subtotal
chocolate, milk, bread = 20, 12, 15.5
print("Cart:\nchocolate\nmilk\nbread\nSubtotal: %.2f kr." % (chocolate + milk + bread))  # 47.50

# Triangle area: base = 5, height = 10
bas, höjd = 5, 10
print("A triangle with the base of:", bas, "centimeters and the height of", höjd,
      "centimeters has an area of: %d squarecentimeters" % (bas * höjd / 2))  # (5*10)/2 = 25

# Children born every X seconds in Y years (inaccurate: 30-day months)
minute = 60
hour = minute * 60
day = hour * 24
month = day * 30
year = month * 12

time = 7         # every 7 seconds
years = 5
print("The total number of children born every", time, "seconds during a", years,
      "year time is:", int(years * year / time), "children")

# Children born every X seconds in Y years (accurate: 365-day year)
minute = 60
hour = minute * 60
day = hour * 24
month = day * (365 / 12)
year = month * 12

print("The total number of children born every", time, "seconds during a", years,
      "year time is:", int(years * year / time), "children")
