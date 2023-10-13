from art import logo

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "cant divide with 0"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(logo)
    calculate = True
    num1 = float(input("what's the first number: "))
    for key in operations:
        print(key)
    while calculate:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("what's the next number: "))
        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation: ")
        if answer == "n":
            calculate = False
            calculator()
        else:
            num1 = result

calculator()
