import operator
import math

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '**': operator.pow,
    'sqrt': math.sqrt,
    'log': math.log,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
}

def calculate(num1, num2, operator):
    if operator in ['sqrt', 'log', 'sin', 'cos', 'tan']:
        return operators[operator](num1)
    else:
        return operators[operator](num1, num2)

def main():
    history = []
    print("Advanced Scientific Calculator with History\n")
    print("Operators: +, -, *, /, %, **, sqrt, log, sin, cos, tan\n")

    while True:
        operator = input("Enter operator: ")

        if operator in ['sqrt', 'log', 'sin', 'cos', 'tan']:
            num1 = float(input("Enter number: "))
            result = calculate(num1, None, operator)
            history.append((operator, num1, result))
            print(f"\nResult: {operator}({num1}) = {result}")
        elif operator in operators:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = calculate(num1, num2, operator)
            history.append((num1, operator, num2, result))
            print(f"\nResult: {num1} {operator} {num2} = {result}")
        else:
            print("\nInvalid operator. Try again.")
            continue

        repeat = input("\nWould you like to perform another calculation? (y/n) ")
        if repeat.lower() != 'y':
            break

    if history:
        print("\nCalculation History:")
        for calculation in history:
            if len(calculation) == 3:
                print(f"{calculation[0]}({calculation[1]}) = {calculation[2]}")
            else:
                print(f"{calculation[0]} {calculation[1]} {calculation[2]} = {calculation[3]}")
    else:
        print("\nNo calculations to display.")

if __name__ == '__main__':
    main()
