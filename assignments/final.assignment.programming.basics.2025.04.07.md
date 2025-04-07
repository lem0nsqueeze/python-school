## **1. Conditions in Programming (If Statements)**  

### **What are conditions?**  
Conditions are used in programming to control which parts of the code should run based on certain rules. In Python, `if`, `elif`, and `else` are used to create conditions.

### **Example 1: Simple Conditions**
```python
x = int(input("Enter a number: "))

if x > 0:
    print("The number is positive")
elif x < 0:
    print("The number is negative")
else:
    print("The number is zero")
```

### **Example 2: Conditions with multiple expressions**
```python
age = int(input("Enter your age: "))

if age >= 18 and age < 65:
    print("You are an adult.")
elif age >= 65:
    print("You are a senior.")
else:
    print("You are a minor.")
```

### **Exercises**
1. Write a program that asks for a person's body temperature and determines if they have hypothermia (< 35°C), normal temperature (35–37.5°C), or fever (> 37.5°C).
2. Create a program where the user enters two numbers, and the program determines which one is greater.
3. Write a menu where the user selects a dish and the program responds with the required ingredients.

## **2. Loops in Programming**

### **What are loops?**  
Loops are used to repeat code several times without having to write the same code again and again.

### **For Loop**
```python
for i in range(1, 6):
    print(f"Iteration number {i}")
```

### **While Loop**
```python
x = 0
while x < 5:
    print(f"x is {x}")
    x += 1
```

### **Exercises**
1. Create a for loop that prints all even numbers between 1 and 20.
2. Write a guessing game where the program selects a random number between 1 and 10, and the user keeps guessing until they get it right.
3. Create a while loop that asks the user to enter a name and ends when they type "exit".

## **3. Lists and Tuples**  

### **What are lists and tuples?**  
- Lists are used to store multiple values in an ordered sequence.  
- Tuples work the same way but cannot be changed after creation.

### **Example: List**
```python
fruits = ["apple", "banana", "orange"]
fruits.append("grape")  # Adds an element
print(fruits[1])  # Output: banana
```

### **Example: Tuple**
```python
colors = ("red", "green", "blue")
print(colors[0])  # Output: red
```

### **Exercises**
1. Create a list of your five favorite movies and print them with a for loop.
2. Create a tuple with three car brands and try to change one. What happens?
3. Make a list where the user can add and remove items interactively.

## **4. Dictionaries and Sets**  

### **What are dictionaries and sets?**  
- Dictionaries store key-value pairs (e.g., name and age).
- Sets are a collection of unique values.

### **Example: Dictionary**
```python
person = {"name": "Alice", "age": 25}
print(person["name"])  # Output: Alice
person["city"] = "Stockholm"
```

### **Example: Set**
```python
unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)  # Output: {1, 2, 3, 4}
```

### **Exercises**
1. Create a dictionary where the key is a person's name and the value is their favorite color.
2. Create two sets and find common elements using `.intersection()`.

## **5. Functions in Python**  

### **What are functions?**  
Functions allow us to reuse code and keep our programs organized.

### **Example**
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

### **Exercises**
1. Write a function that counts the number of vowels in a string.
2. Create a function that checks if a number is odd or even.

## **6. Error Handling**  

### **What is error handling?**  
Errors can be handled using `try-except`.

### **Example**
```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Enter a valid integer!")
```

### **Exercises**
1. Try to access an index in a list that doesn't exist and handle the error.
2. Create a program where the user enters text instead of a number, and handle the error.

## **7. Reusable and Modular Code**  

### **What are modules?**  
You can import functions from other files.

### **Example: Create a module**  
File: `mymodule.py`
```python
def square(x):
    return x * x
```

Main program:
```python
import mymodule
print(mymodule.square(4))  # Output: 16
```

### **Exercises**
1. Create a module that contains a function that calculates the area of a circle.
2. Import a built-in module, such as `math`, and use `math.sqrt()`.

### **Challenge**  
Write a program where the user can:  
1. Enter name and age  
2. Get a welcome message based on age  
3. Get their favorite number squared with a function  
4. See error messages if they enter invalid values  

