# Q8. Let’s create a Simple Calculator that performs arithmetic operations.

# Create a function calculator(a, b, operation) that performs addition, subtraction, multiplication, or division based on the operation parameter.

# The operation parameter can have values ‘+’, ‘−’, ‘*’, and ‘/’.

a = int(input("Enter a: "))
b = int(input("Enter b: "))
operation = input("Enter Operations (+, -, *, /): ")

def calculator(a,b,operation):
    if(operation == "+"):
        return a + b
    elif(operation == "-"):
        return a - b
    
    elif(operation == "*"):
        return a * b
    else:
        return a / b
    
print(calculator(a,b,operation))