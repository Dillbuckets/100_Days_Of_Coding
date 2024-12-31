def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide, 
    }

from calculator_art import logo
import os

def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))

    continue_calculations = True
    while continue_calculations:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the symbols above: ")

        num2 = float(input("What is the next number?: "))

        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        more = input(f"Type \"y\" to continue calculating with {answer}, type \"n\" to restart, and type anything else to exit.: ")
        if more == "y":
            num1 = answer
        elif more == "n":
            continue_calculations = False
            os.system('clear')
            calculator()
        else:
            continue_calculations = False
            os.system('clear')

calculator()