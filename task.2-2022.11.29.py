#!/usr/bin/env python3

import socket

print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

# ====================================================================
# TASK:
# Marko and Samir need help again!
#
# Write a Python script that:
#
# - Asks the user to input their scores for the following subjects:
#   • Data Science
#   • Data and Networking
#   • Networking
#   • Administration
#   • Programming
#
# - Calculates the average score (total / number of subjects)
#
# - Based on the average, prints a letter grade:
#     90–100 : A
#     80–89  : B
#     70–79  : C
#     60–69  : D
#     50–59  : E
#     < 50   : "What a waste of time... Your average grade is F"
#
# - If the average is out of range (e.g., above 100 or negative), show an error.
#
# Try solving it on your own first!
# 
# >>> NO PEEKING BELOW THIS LINE UNTIL YOU'VE TRIED! <<<
# ====================================================================
















# ========================
# SOLUTION (NO PEEKING!)
# ========================

print("Input your total score for the following subjects:")
x = float(input("Data Science: "))
y = float(input("Data and Networking: "))
z = float(input("Networking: "))
a = float(input("Administration: "))
b = float(input("Programming: "))

total = x + y + z + a + b
avg = total / 5

if 90 <= avg <= 100:
    print("Your average grade is: A")
elif 80 <= avg < 90:
    print("Your average grade is: B")
elif 70 <= avg < 80:
    print("Your average grade is: C")
elif 60 <= avg < 70:
    print("Your average grade is: D")
elif 50 <= avg < 60:
    print("Your average grade is: E")
elif 0 <= avg < 50:
    print("What a waste of time...\nYour average grade is F")
else:
    print("Please enter numeric values between 0 and 100")