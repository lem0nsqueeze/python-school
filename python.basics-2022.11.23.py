#!/usr/bin/env python
import socket
print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

print(7**2)
# 49

print(7//2)
# 3

print(49**0.5)
# 49

print(2**6)
# 64

print(9/2, "and", 9//2)
# 4.5 and 4

print(11/6, "and", 11//6)
# 1.8333333333333333 and 1

print(21/8, "and", 21//8)
# 2.625 and 2

print("a rectangle has the width of 3 cm and the length of 4 cm.")
# a rectangle has the width of 3 cm and the length of 4 cm. 
print("The circumference is", (3+4)*2, "centimeters.")
# The circumference is: 14 centimeters
print("the area is", (3*4), "squarecentimeters.")
# the area is: 12 squarecentimeters

print("a rectangle has the width of 3 cm and the length of 4 cm. \nThe circumference is: " f"{(3+4)*2}"" centimeters" "\nthe area is: " f"{3*4}" " squarecentimeters")
# a rectangle has the width of 3 cm and the length of 4 cm. 
# The circumference is: 14 centimeters
# the area is: 12 squarecentimeters

x = 10
y = 15
print(x*y)
# 150

# - x=width
# - y=the length of
x = 3
y = 4
print("a rectangle has the width of 3cm and the length of 4cm. \nThe circumference is: " f"{(x+y)*2}"" centimeters" "\nthe area is: " f"{x*y}" " squarecentimeters")
# a rectangle has the width of 3cm and the length of 4cm.
# The circumference is: 14 centimeters
# the area is: 12 squarecentimeters

error="CRITICAL ERROR, PLEASE TRY AGAIN!"
print(error)

a=5
b=10
c=(2*a)-(3*b)
print(c)
# -20

x,y=5,8
print("a rectangle has the width of 5cm and the length of 8cm. \nThe circumference is: " f"{(x+y)*2}"" centimeters" "\nthe area is: " f"{x*y}" " squarecentimeters")
# The circumference is: 26 centimeters
# the area is: 40 squarecentimeters

x,y=92,230
print("a rectangle has the width of 92cm and the length of 230cm. \nThe circumference is: " f"{(x+y)*2}"" centimeters" "\nthe area is: " f"{x*y}" " squarecentimeters")
# The circumference is: 644 centimeters
# the area is: 21160 squarecentimeters

x,y=1,3
print("a rectangle has the width of 1m and the length of 3m. \nThe circumference is: " f"{(x+y)*2}"" meter" "\nthe area is: " f"{x*y}" " squaremeters")
# The circumference is: 8 meter
# the area is: 3 squaremeters

x,y=2,3
print(x*y)

chocolate,milk,bread=20,12,15.5
print("cart:\n" "chocolate\nmilk\nbread\n" "subtotal: %0.2f kr." % (chocolate+milk+bread))
# cart:
# chocolate
# milk
# bread
# subtotal: 47.50 kr.

bas,höjd=5,10
print("a triangle with the base of:" f" {bas}" " centimeters and the height of" f" {höjd}" " centimeters " "has an area of: %d squarecentimeters" % (bas*höjd/2))
# a triangle with the base of: 5 centimeters and the height of 10 centimeters has an area of: 25 squarecentimeters

# - purpose: get an inaccurate amount of children born each year (assume that a month is 30 days..)
minute=60
hour=(minute*60)
day=(hour*24)
month=(day*30)
year=(month*12)
# - please only edit time/year to calculate how many children are born each second in x amount of years...
time=7
years=5
print("the total number of children born every" f" {time} seconds " "during a" f" {years} year time is:"" %d children" % (years*year/time))
# the total number of children born every 7 seconds during a 5 year time is: 22217142 children

# - now get the accurate amount of children born each second in x amount of years
minute=60
hour=(minute*60)
day=(hour*24)
month=(day*365/12)
year=(month*12)
# - please only edit time/year to calculate how many children are born each second in x amount of years...
time=7
years=5
print("the total number of children born every" f" {time} seconds " "during a" f" {years} year time is:"" %d children" % (years*year/time))
# the total number of children born every 7 seconds during a 5 year time is: 22217142 children
