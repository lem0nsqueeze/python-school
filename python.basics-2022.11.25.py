#!/usr/bin/env python
import socket
print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

# -
namn=input("what is your name?")
print(namn)

# -
age=int(input("how old are you?"))
height=float(input("how tall are you?"))
print("your age is:",age, "your height is:", height)
# - eller
age=int(input("how old are you?"))
height=float(input("how tall are you?"))
print("you are" f" {age} years old " "and" f" {height} cm tall")

# -
tal=input("write a number: ")
print(5*tal)
# write a number: 8
# 88888

# -
tal=int(input("write a number: "))
print(5*tal)
# write in a number: 8
# 40

# - ',' = space, '+' no space
namn=input("what is your name? ")
print("Hello",namn+","+"\nWelcome to SATS!")

# -
rate=499
hours=int(input("How many hours would you like to work out?"))
print("Det kostar",rate*hours,"kr.")

# -
rate=499
hours=float(input("How many hours would you like to work out? "))
print("the rate per hour is:" f" {rate} kr/h \n" "your total fee is:" " %d kr." % (rate*hours))

# -
print(round(663.671245, 2))
# 663.67

# -
namn=input("Hello,\nState first- and lastname: ")
print("Hello",namn+","+"\nWelcome to 2226 Group!")
fortsätt=input("This is a customer surveym, would you like to continue?")
print("How nice of you...")
age=int(input("how old are you? "))
print("Interesting...")
print("That means that you will be taking your pension in" " %d years" %(65-age))
height=float(input("What is your height(m)? "))
print("Oh wow are you actually %d cm tall?" %(height*100))
puls=input("Do you have any idea what your maximum pulserate is? ")
print("Your maximum pulserate is %d" %(220-age))
hjälp=input("How can i further assist you? ")
print("Ok, please hold... taking a coffee break...")

# -
print("please input 4 decimal numbers.\nwe will multpiply the numbers and get a total value.")
first=float(input("State the first value: "))
second=float(input("State the second value: "))
third=float(input("State the third value: "))
fourth=float(input("State the fourth value: "))
result=(first*second*third*fourth)
print("The total value of the four decimal numbers is: %0.2f" %(result))

# -
for loop in range(5):
    print("this is a loop")

# -
for loop in range(1,6):
    print(loop)
# 1
# 2
# 3
# 4
# 5

# -
for firstname in range(15):
    print("firstname")
for lastname in range(20):
    print("lastname")

