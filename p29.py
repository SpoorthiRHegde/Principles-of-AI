# Simple calculator to add, subtract, multiply, and divide
def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b
    else:
        return "Invalid operation"

# Test the function
a, b = 10, 5
print(f"{a} + {b} = {calculator(a, b, 'add')}")
print(f"{a} - {b} = {calculator(a, b, 'subtract')}")
print(f"{a} * {b} = {calculator(a, b, 'multiply')}")
print(f"{a} / {b} = {calculator(a, b, 'divide')}")
