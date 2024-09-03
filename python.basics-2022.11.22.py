#!/usr/bin/env python
import socket
print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

print(4 + 2)
# 6

print(4 - 2)
# 2

print(4 * 2)
# 8

print(4 + 2)
# 6

print(4 - 2)
# 2

print(6 / 2)
# 3

print(38 + 11 + 8)
# 57

print("38 + 11 + 8")
# 38 + 11 + 8

print("you'll have to pay:")
print(38 + 11 + 8)
# you'll have to pay
# 57

print("you'll have to pay:", 38 + 11 + 8, "kr.")
# you'll have to pay: 57 kr.

# - issue: space before '57' on line 36
print("you'll have to pay:\n",38 + 11 + 8, "kr.")
# you'll have to pay:
#  57 kr.

# - solution for line 36:
print("you'll have to pay:\n" f"{38 + 11 + 8}" "kr.")
print("you'll have to pay:\n%d kr." % (38 + 11 + 8))
# you'll have to pay:
# 57 kr.

print("Languages:\nPython\tJava\nJavaScript")
# Languages:
# Python    Java
# Javascript

print(12 - 7)
print(24/3+9)
print(8*2* (5-3)+16/4 -1)
# 5
# 17.0
# 35.0

print("Hello!\nHow are you?")
# Hello!
# How are you?

print("1" + "1")
print(3 * "1")
print(1 +1)
print(1 * 3)
# 11
# 111
# 2
# 3

print("hello" , "hello")
# hello hello
print("hello\t" *10)
# hello hello hello hello hello hello hello hello hello hello

print("If you drive at a speed of 70 km/h in 1.5 hours, then you can make a")
print(70 *1.5)
print("km. trip")
# If you drive at a speed of 70 km/h in 1.5 hours, then you can make a
# 105.0
# km. trip
print("If you drive at a speed of 70 km/h in 1.5 hours, then you can make a", (70*1.5), "km. trip")
# If you drive at a speed of 70 km/h in 1.5 hours, then you can make a 105.0 km. trip
