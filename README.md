


# Python Solutions for Programming Test

These solutions are written in **Python**. Each problem is saved in a separate `.py` file and contains comments explaining the logic and functionality of the code.

---

## 🧮 Problem 1: Calculator Using a Class

### Description:
Create a calculator that can perform Addition, Subtraction, Multiplication, and Division using a class.  
Inputs: `a` (float), `b` (float), `operation` (string)

### File: `problem1.py`

```python
# Language: Python
# Problem 1: Calculator using a class
# This program performs basic arithmetic operations based on user input.

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Division by zero is not allowed."

# Taking user input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

calc = Calculator(a, b)

if operation == "add":
    print("Result:", calc.add())
elif operation == "subtract":
    print("Result:", calc.subtract())
elif operation == "multiply":
    print("Result:", calc.multiply())
elif operation == "divide":
    print("Result:", calc.divide())
else:
    print("Invalid operation.")


2.# Language: Python
# Problem 2: Generate a series of odd numbers
# This program generates the first 'a' odd numbers.

a = int(input("Enter a: "))

for i in range(a):
    print(2 * i + 1, end=", " if i < a - 1 else "\n")


3.
# Language: Python
# Problem 3: Generate a series of odd numbers up to a given limit
# This program prints odd numbers from 1 up to 'a'.

a = int(input("Enter a: "))

for i in range(1, a + 1, 2):
    print(i, end=", " if i + 2 <= a else "\n")


4.
# Language: Python
# Problem 4: Count multiples of numbers 1 to 9 in a list
# This program counts how many numbers in the list are divisible by each number from 1 to 9.

numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

result = {i: 0 for i in range(1, 10)}

for i in range(1, 10):
    for num in numbers:
        if num % i == 0:
            result[i] += 1

print(result)
