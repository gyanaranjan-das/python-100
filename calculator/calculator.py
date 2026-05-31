

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

print("=" * 40)
print("ADVANCED CLI CALCULATOR")
print("Type 'exit' to quit")
print("=" * 40)

while True:
    expression = input(">>>")
    
    if expression.lower() == "exit":
        print("Calculator closed.")
        break
    
    try:
        result = eval(
            expression,
            {"__builtins__":None},
            {}
        )
        print("Result =", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    
    except:
        print("Invalid expression")
    