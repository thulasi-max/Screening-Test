class Calculator:
    def __init__(self, a, b, operation):
        self.a = float(a)
        self.b = float(b)
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "addition":
            return self.a + self.b
        elif self.operation == "subtraction":
            return self.a - self.b
        elif self.operation == "multiplication":
            return self.a * self.b
        elif self.operation == "division":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Error: Invalid operation"

# Example usage
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
operation = input("Enter operation (Addition, Subtraction, Multiplication, Division): ")

calc = Calculator(a, b, operation)
result = calc.calculate()
print("Result:", result)
