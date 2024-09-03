#!/usr/bin/env python
import socket
print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

# Write a script that tells the user to input their in scores for each subject,
# then divide the sum by amount of subjects to get the average grade.
# - If the total score is between 90-100, the program will print 'Your average grade is:' A'
# - If the total score is between 80-89, the program will print 'Your average grade is:' B'
# - If the total score is between 70-79, the program will print 'Your average grade is:' C'
# - If the total score is between 60-69, the program will print 'Your average grade is:' D'
# - If the total score is between 50-59, the program will print 'Your average grade is:' E'
# - If the total score is less than 50, the program will print 'What a waste of time...'

print('input your total score for the following subjects: ')
x = float(input('Data science: '))
y = float(input('Data and networking: '))
z = float(input('Networking: '))
a = float(input('Administration: '))
b = float(input('Programming: ' ))

total = x+y+z+a+b
avg = total/5

if avg>=90 and avg<=100:
    print('Your average grade is: A')
elif avg>=80 and avg<89:
    print('Your average grade is: B')
elif avg>=70 and avg<79:
    print('Your average grade is: C')
elif avg>=60 and avg<69:
    print('Your average grade is: D')
elif avg>=50 and avg<59:
    print('Your average grade is: E')
elif avg>=0 and avg<50:
    print('What a waste of time...\nYour average grade is F')

else:
    print('Please enter a numeric value from 0 to 100')

