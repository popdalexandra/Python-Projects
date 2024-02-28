from day10_art import logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

# recursion
def calculation():
    print(logo)  

    num1 = float(input("What's the first number? "))

    for symbol in operations:
        print(symbol)

    continue_calc = True

    while continue_calc:
        operation_symbol = input("Pick an operation! ")
        num2 = float(input("What's the next number? "))

        # if operation_symbol == "+":
        #     answer = add(num1, num2)
        # elif operation_symbol == "-":
        #     answer = substract(num1, num2)
        # elif operation_symbol == "*":
        #     answer = multiply(num1, num2)
        # elif operation_symbol == "/":
        #     answer = divide(num1, num2)

        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            continue_calc = False
            calculation()

calculation()