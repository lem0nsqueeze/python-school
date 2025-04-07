#!/usr/bin/env python3

import socket

print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

# ======================================================
# if-elif-else version
lang = input("What programming language do you want to learn? ")

if lang == "JavaScript":
    print("You can become a web developer.")
elif lang == "Python":
    print("You can become a Data Scientist.")
elif lang == "PHP":
    print("You can become a backend developer.")
elif lang == "Solidity":
    print("You can become a Blockchain developer.")
elif lang == "Java":
    print("You can become a mobile app developer.")
else:
    print("The language doesn't matter, what matters is solving problems.")

# ======================================================
# match-case version (Python 3.10+)

lang = input("What programming language do you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")
    case "Python":
        print("You can become a Data Scientist.")
    case "PHP":
        print("You can become a backend developer.")
    case "Solidity":
        print("You can become a Blockchain developer.")
    case "Java":
        print("You can become a mobile app developer.")
    case _:
        print("The language doesn't matter, what matters is solving problems.")

# ======================================================
# Grading system example - version 1 (rounded)

points = float(input("Enter your score (0–100): "))
grade = int(points // 10)

match grade:
    case 0 | 1 | 2 | 3 | 4:
        print("Fail")
    case 5:
        print("E")
    case 6:
        print("D")
    case 7:
        print("C")
    case 8:
        print("B")
    case 9 | 10:
        print("A")
    case _:
        print("Please enter a numeric value between 0–100.")

# ======================================================
# Grading system example - version 2 (range checks)

points = float(input("Enter your score (0–100): "))

match points:
    case p if 0 <= p < 50:
        print("Fail")
    case p if 50 <= p <= 59:
        print("E")
    case p if 60 <= p <= 69:
        print("D")
    case p if 70 <= p <= 79:
        print("C")
    case p if 80 <= p <= 89:
        print("B")
    case p if 90 <= p <= 100:
        print("A")
    case _:
        print("Please enter a numeric value between 0–100.")

# ======================================================
# MATCH vs IF-ELIF-ELSE — Summary

"""
MATCH-CASE (Python 3.10+) vs IF-ELIF-ELSE

Benefits of match-case:
1. Readability — cleaner and easier to read than long if-elif chains.
2. Pattern Matching — supports type, structure, and value patterns.
3. Efficiency — internally optimized for multiple conditions.
4. Maintainability — easier to update and expand.
5. Clean syntax comparison:

match lang:
    case "JavaScript":
        print("Web developer.")
    case "Python":
        print("Data Scientist.")
    case _:
        print("Solve problems.")

vs

if lang == "JavaScript":
    print("Web developer.")
elif lang == "Python":
    print("Data Scientist.")
else:
    print("Solve problems.")
"""