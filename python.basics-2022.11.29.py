#!/usr/bin/env python
import socket
print("This is a vodka-bottle-documentation, sorry, no automation at this time, :-/")
raise SystemExit

for n in range(1, 17, 3):
	print(n)

for n in range(1, 5):
	print('jensen!')

while True:
	for x in range(1, 12):
		for y in range(1, 101):
			for z in range(-100, 6):
				print (x, y, z)
				continue

for n in range(0, 102, 2):
	print(n)

for n in range(0, 51):
	print (2*n)

number = 1
for n in range(1, 11):
   print(number, 'x', n, '=', number*n)

for x in range(1,11):
    print('\n\nTable %d\n' %(x))
    for y in range(1,11):
        print('%d x %d = %d' % (x, y, x*y))

num = 3
if num > 0:
	print(num, "is a positive number.")
	print("This is always printed.")

##########################################################
# python script
# - copy and paste all the lines below and paste to
# - a file and save the file as 'patient.py'
# - then run the program
##########################################################

#!/usr/bin/env python
import os

# main function
def main():

	# loop
    specify_input = ''
while True:
    specify_input = input('Are you an adult? y/n: ')

    if specify_input.lower() == 'y':
        print('Your recommended intake is 750 mg/day')
        break
    elif specify_input.lower() == 'n':
        print('Your recommended intake is 500mg/day')
        break
    else:
        print("please answer with a 'y' or 'n' ")
        continue
        
if __name__ == '__main__':
    # invokes main function
    main()

##########################################################

#!/usr/bin/env python
import os

# main function
def main():

	# loop
    weight = ''
while True:
    weight = float (input('what is your weight? '))

    if weight < 20:
        print('Your recommended intake is 500 mg/day')
        break
    elif 20 <= weight <= 40:
        print('Your recommended intake is 750mg/day')
        break
    elif 41 <= weight <= 60:
        print('Your recommended intake is 1000mg/day')
        break
    else:
        print('Your recommended intake is 1000mg/day')
        break
        
if __name__ == '__main__':
    # invokes main function
    main()

##########################################################
