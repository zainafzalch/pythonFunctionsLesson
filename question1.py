# 1. The Calculator App

# Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.

# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

# Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

def addition (number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

op = input("Addition, Subtraction, Multiplication or Division: ").lower()

def arithmeticOperation(number1=int(input("Enter first number: ")), number2=int(input("Enter second number: "))):
    result = 0
    
    if(op == "addition"):
        result = addition(number1, number2)

    if(op == "subtraction"):
        result = subtraction(number1, number2)

    if(op == "multiplication"):
        result = multiplication(number1, number2)

    try:
        if(op == "division"):
            result = division(number1, number2)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    return result

print(arithmeticOperation())