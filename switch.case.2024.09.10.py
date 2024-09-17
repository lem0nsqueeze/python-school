#!/usr/bin/env python
import socket
print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

# if-elif-else structure
lang = input("What's the programming language you want to learn? ")

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

## switch case
lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")

    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")

# Example 1 - without "if"
points = float(input("Ange ditt poäng: "))

rounded_points = int(points // 10)

match rounded_points:
    case 0 | 1 | 2 | 3 | 4:
        print("Ej Godkänd")
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
        print("Ange ett numeriskt värde mellan 0-100")

# Example 2 - with "if"
points = float(input("Ange ditt poäng: "))

match points:
    case p if 0 <= p < 50:
        print("Ej Godkänd")
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
        print("Ange ett numeriskt värde mellan 0-100")

# ===========================================================================
# NAME
#     switch-case vs if-elif-else in Python
#
# DESCRIPTION
#     The 'match' statement (similar to switch-case in other languages) was 
#     introduced in Python 3.10. It provides a more efficient and cleaner way 
#     to handle multiple conditions compared to the traditional 'if-elif-else' 
#     construct. Below are key reasons why 'match-case' is often preferred:
#
# BENEFITS OF SWITCH-CASE (MATCH IN PYTHON):
#
# 1. **Readability**
#     - In a 'match-case', each possible case is clearly separated, resulting
#       in cleaner code.
#     - Eliminates the repetitive 'if' and 'elif' keywords found in long
#       conditional chains, making the logic easier to follow.
#     - Example:
#         match lang:
#             case "JavaScript":
#                 print("Web developer.")
#             case "Python":
#                 print("Data Scientist.")
#             ...
#
# 2. **Pattern Matching**
#     - Unlike 'if-elif-else', Python's 'match-case' supports pattern matching,
#       allowing more complex conditions like matching types, data structures,
#       or values within lists/tuples.
#     - This advanced capability is beyond simple comparisons in 'if-elif-else'.
#
# 3. **Efficiency**
#     - In scenarios where there are many conditions, 'match-case' may execute 
#       faster because of internal optimizations (such as using a lookup table 
#       or hashing) compared to sequential evaluations in 'if-elif-else'.
#     - This efficiency boost can matter in performance-critical applications.
#
# 4. **Maintainability**
#     - The 'match-case' structure is more maintainable, especially when adding
#       or modifying cases. The logic remains more organized, reducing the 
#       chances of errors when updating or extending conditions.
#
# 5. **Code Example Comparison**:
#     - 'match-case' version:
#         match lang:
#             case "JavaScript":
#                 print("Web developer.")
#             case "Python":
#                 print("Data Scientist.")
#             case _:
#                 print("Solve problems.")
#
#     - 'if-elif-else' version:
#         if lang == "JavaScript":
#             print("Web developer.")
#         elif lang == "Python":
#             print("Data Scientist.")
#         else:
#             print("Solve problems.")
#
# CONCLUSION
#     While both 'if-elif-else' and 'match-case' provide the same basic 
#     functionality, 'match-case' offers better readability, maintainability, 
#     and efficiency, particularly when dealing with multiple conditions or 
#     complex pattern matching scenarios.
# ===========================================================================
