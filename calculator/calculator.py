
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
    expression = input(">>>")
    parts = expression.split()
    
    if len(parts)!= 3:
        print("Use: number operator number (e.g., 2 + 3)")
        continue
        
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

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