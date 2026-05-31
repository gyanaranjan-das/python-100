
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Error: Division by zero is not allowed."
    return a/b


while True:
    num1 = float(input("Enter the first number:"))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number:"))

    if operator == "+":
        print("Result =",add(num1,num2))

    elif operator == "-":
        print("Result =",subtract(num1,num2))
    elif operator == "*":
        print("Result =",multiply(num1,num2))
    elif operator == "/":
        print("Result =",divide(num1,num2))
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        
    if input("Continue? (y/n): ").lower() == 'n':
        break