from day10_art import logo

#calculator functions
def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    should_continue = True
    #Request for numbers and operation
    num1 = float(input("What's the first number: "))
    while should_continue:
        for symbol in operators:
            print(symbol)
        operator = input("Pick an operation sysmbol: ")

        num2 = float(input("What's the second number: "))

        #calculation answer
        function = operators[operator]
        answer = function(num1, num2)

        print(f"{num1} {operator} {num2} = {answer}")

        end_calculator = input(f"Type y to continue calculating with {answer}, or type n to start a new calculation: ")

        if end_calculator == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


#Operators dictionary
operators = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

#App welcome message
print(logo)

calculator()