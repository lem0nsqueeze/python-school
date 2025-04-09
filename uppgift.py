# Import date
from datetime import datetime

# Prompts the user to type their name and age
name = input("Hej vad heter du: ")
age = int(input("Hur gammal är du?: "))

# Calculate the current year
current_year = datetime.now().year

# Calculate current year and adds 100 - your age to tell what year you turn 100
year100 = current_year + (100 - age)

# Prints your name and age and also what year you turn 100
print(f"Hej {name}! Du är {age} år gammal!")
print(f"Du är 100 år gammal år {year100}")